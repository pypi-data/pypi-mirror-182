# SPDX-License-Identifier: GPL-3.0-or-later

"""General-Purpose Text Classifier"""

from gptc.compiler import compile as compile
from gptc.classifier import Classifier as Classifier
from gptc.pack import pack as pack
from gptc.model import Model as Model, deserialize as deserialize
from gptc.tokenizer import normalize as normalize
from gptc.exceptions import (
    GPTCError as GPTCError,
    ModelError as ModelError,
    InvalidModelError as InvalidModelError,
)
