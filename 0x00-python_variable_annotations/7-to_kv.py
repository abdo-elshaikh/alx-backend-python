#!/usr/bin/env python3
"""modul"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Converts a string and an int/float to a tuple"""
    return [k, v ** 2]
