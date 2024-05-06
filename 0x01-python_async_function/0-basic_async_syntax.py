#!/usr/bin/env python3
"""modul"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns the number of seconds"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
