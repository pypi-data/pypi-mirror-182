from __future__ import annotations

from typing import Any



class Noll:
    """
    A dummy object that provides methods that do nothing
    and comparisons that always return False.
    """

    singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = super().__new__(cls, *args, **kwargs)
        return cls.singleton


    def _getter(self, key: Any) -> Noll:
        return self

    def _setter(self, key: Any, value: Any):
        pass

    __getattr__ = __getitem__ = _getter
    __setattr__ = __setitem__ = _setter


    def __call__(self, *args, **kwargs):
        pass

    
    def _compare(self, other: Any) -> bool:
        return False
 
    __lt__ = \
    __le__ = \
    __eq__ = \
    __ne__ = \
    __gt__ = \
    __ge__ = \
        _compare

    def _arithmetic(self, other: Any) -> Any:
        return other

    __add__ = \
    __sub__ = \
    __mul__ = \
    __matmul__ = \
    __truediv__ = \
    __floordiv__ = \
        _arithmetic


    def __repr__(self) -> str:
        return ""

    def __str__(self) -> str:
        return ""

    def __bytes__(self) -> bytes:
        return b""
    

    def __abs__(self) -> int:
        return 0
    def __int__(self) -> int:
        return 0
    def __float__(self) -> float:
        return 0.0
    def __complex__(self) -> complex:
        return 0j