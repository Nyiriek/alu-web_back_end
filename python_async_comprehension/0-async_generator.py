#!/usr/bin/env python3
"""
The coroutine will loop 10 times, each
time asynchronously wait 1 second, then yield arandom number between 0 and 10. Use the random module.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async Generator

    Yields:
        float: A random float number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
