#!/usr/bin/env python3
"""modul"""
from asyncio import sleep
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns the number of seconds"""
    delay = random.uniform(0, max_delay)
    await sleep(delay)
    return delay
