"""
This module contains `detadict` class.
"""
from os import environ
from typing import Iterator, MutableMapping, TypeVar

from deta import Deta

_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_VT_co = TypeVar("_VT_co")
_T_co = TypeVar("_T_co")


class detadict(MutableMapping):
    """
    Python dict with Deta backend.

    Require `DETA_PROJECT_KEY` environ variable.
    """

    def __init__(self):  # pylint: disable=super-init-not-called
        self._deta = Deta(environ["DETA_PROJECT_KEY"])
        self._base = self._deta.Base("detadict")
        if not self._base.get("detadict"):
            self._base.insert({}, "detadict")

    def __getitem__(self, k: _KT) -> _VT_co:
        d = self._base.get("detadict")
        return d[k]

    def __setitem__(self, k: _KT, v: _VT) -> None:
        self._base.update({k: v}, "detadict")

    def __delitem__(self, v: _KT) -> None:
        self._base.update({v: self._base.util.trim()}, "detadict")

    def __iter__(self) -> Iterator[_T_co]:
        d = self._base.get("detadict")
        del d["key"]
        return iter(d)

    def __len__(self) -> int:
        return len(self._base.get("detadict")) - 1


__all__ = ["detadict"]
