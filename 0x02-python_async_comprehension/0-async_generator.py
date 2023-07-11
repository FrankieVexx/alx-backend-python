#!/usr/bin/env python3
"""create an async generator"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times, wait for 1 second after each loop"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
