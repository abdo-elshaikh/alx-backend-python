#!/usr/bin/env python3
"""module with async generator"""
import asyncio
import random
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """Async generator returning `n` random numbers between 0 and 1"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
