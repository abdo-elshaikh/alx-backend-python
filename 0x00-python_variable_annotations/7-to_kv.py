#!/usr/bin/env python3
"""modul"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a string and an int/float to a tuple"""
    return [k, v ** 2]
