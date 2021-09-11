"""
This module contains classes that will be used to replace native python types.
"""
from typing import Dict, List


class DetaList(List):
    """
    A native list type replacement.
    """

    ...


class DetaDict(Dict):
    """
    A native dict type replacement.
    """

    ...


__all__ = [
    "DetaList",
    "DetaDict",
]
