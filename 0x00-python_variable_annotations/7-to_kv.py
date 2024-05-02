#!/usr/bin/env python3
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    return [k, v ** 2]
