#!/usr/bin/env python3
"""modul"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """returns a function that multiplies a float"""
    def multiply(n: float) -> float:
        """returns a function that multiplies"""
        return n * multiplier
    return multiply
