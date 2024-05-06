#!/usr/bin/env python3
"""modul"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Wait for a given number of seconds"""
    delayes = []
    for i in range(n):
        delayes.append(wait_random(max_delay))
        i += 1
    return await asyncio.gather(*delayes)
