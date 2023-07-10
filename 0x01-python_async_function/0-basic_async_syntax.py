#!/usr/bin/env python3
""" creating async coroutines that returns the delays"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async function to return delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
