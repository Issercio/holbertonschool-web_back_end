#!/usr/bin/env python3
"""Measure runtime of running async_comprehension concurrently."""

import asyncio
import time
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension 4 times and return total runtime."""
    start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    return end - start
