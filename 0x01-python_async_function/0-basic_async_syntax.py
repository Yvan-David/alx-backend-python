#!/usr/bin/env python3
import asyncio
import random

""" module about asyncio functions """


async def wait_random(max_delay=10):
    """ function that uses asyncio """
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
