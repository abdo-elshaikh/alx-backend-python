#!/usr/bin/env python3

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
