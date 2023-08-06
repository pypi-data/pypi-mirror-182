# SPDX-License-Identifier: GPL-3.0-or-later

import gptc.tokenizer
from gptc.exceptions import InvalidModelError
import gptc.weighting
from typing import Iterable, Mapping, List, Dict, Union, cast, BinaryIO
import json


class Model:
    def __init__(
        self,
        weights: Dict[int, List[int]],
        names: List[str],
        max_ngram_length: int,
        hash_algorithm: str,
    ):
        self.weights = weights
        self.names = names
        self.max_ngram_length = max_ngram_length
        self.hash_algorithm = hash_algorithm

    def confidence(self, text: str, max_ngram_length: int) -> Dict[str, float]:
        """Classify text with confidence.

        Parameters
        ----------
        text : str
            The text to classify

        max_ngram_length : int
            The maximum ngram length to use in classifying

        Returns
        -------
        dict
            {category:probability, category:probability...} or {} if no words
            matching any categories in the model were found

        """

        model = self.weights

        tokens = gptc.tokenizer.hash(
            gptc.tokenizer.tokenize(
                text, min(max_ngram_length, self.max_ngram_length)
            ),
            self.hash_algorithm,
        )
        numbered_probs: Dict[int, float] = {}
        for word in tokens:
            try:
                weighted_numbers = gptc.weighting.weight(
                    [i / 65535 for i in cast(List[float], model[word])]
                )
                for category, value in enumerate(weighted_numbers):
                    try:
                        numbered_probs[category] += value
                    except KeyError:
                        numbered_probs[category] = value
            except KeyError:
                pass
        total = sum(numbered_probs.values())
        probs: Dict[str, float] = {
            self.names[category]: value / total
            for category, value in numbered_probs.items()
        }
        return probs

    def get(self, token: str) -> Dict[str, float]:
        try:
            weights = self.weights[
                gptc.tokenizer.hash_single(
                    gptc.tokenizer.normalize(token), self.hash_algorithm
                )
            ]
        except KeyError:
            return {}
        return {
            category: weights[index] / 65535
            for index, category in enumerate(self.names)
        }

    def serialize(self, file: BinaryIO) -> None:
        file.write(b"GPTC model v5\n")
        file.write(
            json.dumps(
                {
                    "names": self.names,
                    "max_ngram_length": self.max_ngram_length,
                    "hash_algorithm": self.hash_algorithm,
                }
            ).encode("utf-8")
            + b"\n"
        )
        for word, weights in self.weights.items():
            file.write(
                word.to_bytes(6, "big")
                + b"".join([weight.to_bytes(2, "big") for weight in weights])
            )


def deserialize(encoded_model: BinaryIO) -> Model:
    prefix = encoded_model.read(14)
    if prefix != b"GPTC model v5\n":
        raise InvalidModelError()

    config_json = b""
    while True:
        byte = encoded_model.read(1)
        if byte == b"\n":
            break
        elif byte == b"":
            raise InvalidModelError()
        else:
            config_json += byte

    try:
        config = json.loads(config_json.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise InvalidModelError()

    try:
        names = config["names"]
        max_ngram_length = config["max_ngram_length"]
        hash_algorithm = config["hash_algorithm"]
    except KeyError:
        raise InvalidModelError()

    if not (
        isinstance(names, list) and isinstance(max_ngram_length, int)
    ) or not all([isinstance(name, str) for name in names]):
        raise InvalidModelError()

    weight_code_length = 6 + 2 * len(names)

    weights: Dict[int, List[int]] = {}

    while True:
        code = encoded_model.read(weight_code_length)
        if not code:
            break
        elif len(code) != weight_code_length:
            raise InvalidModelError()

        weights[int.from_bytes(code[:6], "big")] = [
            int.from_bytes(value, "big")
            for value in [code[x : x + 2] for x in range(6, len(code), 2)]
        ]

    return Model(weights, names, max_ngram_length, hash_algorithm)
