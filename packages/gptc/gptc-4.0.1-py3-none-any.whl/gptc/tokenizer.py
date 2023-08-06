# SPDX-License-Identifier: GPL-3.0-or-later

from typing import List, Union, Callable, Any, cast
import hashlib
import emoji
import unicodedata


def tokenize(text: str, max_ngram_length: int = 1) -> List[str]:
    text = unicodedata.normalize("NFKD", text).lower()
    parts = []
    highest_end = 0
    for emoji_part in emoji.emoji_list(text):
        parts += list(text[highest_end : emoji_part["match_start"]])
        parts.append(emoji_part["emoji"])
        highest_end = emoji_part["match_end"]
    parts += list(text[highest_end:])
    converted_text = [part for part in parts if part]

    tokens = [""]

    for char in converted_text:
        if (
            char.isalpha()
            or char.isnumeric()
            or char == "'"
            or (char in ",." and (" " + tokens[-1])[-1].isnumeric())
        ):
            tokens[-1] += char
        elif emoji.is_emoji(char):
            tokens.append(char)
            tokens.append("")
        elif tokens[-1] != "":
            tokens.append("")

    tokens = [string for string in tokens if string]

    if max_ngram_length == 1:
        return tokens
    else:
        ngrams = []
        for ngram_length in range(1, max_ngram_length + 1):
            for index in range(len(tokens) + 1 - ngram_length):
                ngrams.append(" ".join(tokens[index : index + ngram_length]))
        return ngrams


def _hash_single(token: str, hash_function: type) -> int:
    return int.from_bytes(
        hash_function(token.encode("utf-8")).digest()[:6], "big"
    )


def _get_hash_function(hash_algorithm: str) -> type:
    if hash_algorithm in {
        "sha224",
        "md5",
        "sha512",
        "sha3_256",
        "blake2s",
        "sha3_224",
        "sha1",
        "sha256",
        "sha384",
        "shake_256",
        "blake2b",
        "sha3_512",
        "shake_128",
        "sha3_384",
    }:
        return cast(type, getattr(hashlib, hash_algorithm))
    else:
        raise ValueError("not a valid hash function: " + hash_algorithm)


def hash_single(token: str, hash_algorithm: str) -> int:
    return _hash_single(token, _get_hash_function(hash_algorithm))


def hash(tokens: List[str], hash_algorithm: str) -> List[int]:
    hash_function = _get_hash_function(hash_algorithm)
    return [_hash_single(token, hash_function) for token in tokens]


def normalize(text: str) -> str:
    return " ".join(tokenize(text, 1))
