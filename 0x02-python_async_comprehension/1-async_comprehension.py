#!/usr/bin/env python3
"""async function creator"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns 10 randomly created numbers"""
    results = [i async for i in async_generator()]
    return results
