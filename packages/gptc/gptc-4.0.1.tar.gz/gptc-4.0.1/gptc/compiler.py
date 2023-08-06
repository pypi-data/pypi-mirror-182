# SPDX-License-Identifier: GPL-3.0-or-later

import gptc.tokenizer
import gptc.model
from typing import Iterable, Mapping, List, Dict, Union


def compile(
    raw_model: Iterable[Mapping[str, str]],
    max_ngram_length: int = 1,
    min_count: int = 1,
    hash_algorithm: str = "sha256",
) -> gptc.model.Model:
    """Compile a raw model.

    Parameters
    ----------
    raw_model : list of dict
        A raw GPTC model.

    max_ngram_length : int
        Maximum ngram lenght to compile with.

    Returns
    -------
    dict
        A compiled GPTC model.

    """

    word_counts: Dict[int, Dict[str, int]] = {}
    category_lengths: Dict[str, int] = {}
    names: List[str] = []

    for portion in raw_model:
        text = gptc.tokenizer.hash(
            gptc.tokenizer.tokenize(portion["text"], max_ngram_length),
            hash_algorithm,
        )
        category = portion["category"]

        if not category in names:
            names.append(category)

        category_lengths[category] = category_lengths.get(category, 0) + len(
            text
        )

        for word in text:
            if word in word_counts:
                try:
                    word_counts[word][category] += 1
                except KeyError:
                    word_counts[word][category] = 1
            else:
                word_counts[word] = {category: 1}

    model: Dict[int, List[int]] = {}
    for word, counts in word_counts.items():
        if sum(counts.values()) >= min_count:
            weights = {
                category: value / category_lengths[category]
                for category, value in counts.items()
            }
            total = sum(weights.values())
            new_weights: List[int] = []
            for category in names:
                new_weights.append(
                    round((weights.get(category, 0) / total) * 65535)
                )
            model[word] = new_weights

    return gptc.model.Model(model, names, max_ngram_length, hash_algorithm)
