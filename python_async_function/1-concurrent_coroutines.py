#!/usr/bin/env python3
"""
Importing wait_random from the previous python file
written and writing an async routine called wait_n that takes in
2 int arguments (in this order): n and max_delay.
Spawn wait_random n times with the specified max_delay.
wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using
sort() because of concurrency.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executing multiple coroutines at the same time with async.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of all the delays in ascending
        order (without using sort()).
    """

    delays: List[float] = []
    all_delays: List[float] = []
    for j in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays
