#!/usr/bin/env python3
"""
Module for Cache class to interact with Redis and store data.
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for storing and retrieving data in Redis.
    On initialization, connects to Redis and flushes the database.
    """
    def __init__(self) -> None:
        """
        Initialize the Cache instance, connect to Redis, and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a random key.

        Args:
            data: The data to store (str, bytes, int, or float).

        Returns:
            str: The generated key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
