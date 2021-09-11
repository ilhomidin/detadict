"""
This module contains `detadict` class.
"""
from os import environ

from deta import Deta


class detadict(dict):  # pylint: disable=invalid-name
    """
    Python dict with Deta backend.

    Require `DETA_PROJECT_KEY` environ variable.
    """

    def __init__(self):  # pylint: disable=super-init-not-called
        self._deta = Deta(environ["DETA_PROJECT_KEY"])
        self._base = self._deta.Base("detadict")


__all__ = ["detadict"]
