#!/usr/bin/env python3
"""
Creating a measure_time function with integers n
and max_delay as arguments that measures the total
execution time for wait_n(n, max_delay), and returns total_time
/ n. Your function should return a float.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines.py').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        float: The average time per wait_n execution.
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
