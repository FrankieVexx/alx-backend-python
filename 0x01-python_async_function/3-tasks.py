#!/usr/bin/env python3
import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random
"""takes an integer
max_delay and returns a asyncio.Task.
"""


def task_wait_random(max_delay: int) -> Task:
    """takes an integer
max_delay and returns a asyncio.Task.
"""
    return asyncio.create_task(wait_random(max_delay))
