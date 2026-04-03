def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a method in Redis lists.
    Each time the decorated method is called, its input arguments are appended to a Redis list
    named '<method_name>:inputs', and its output is appended to '<method_name>:outputs'.
    This allows tracking of all calls and their results for the decorated method.
    Args:
        method: The method to decorate.
    Returns:
        Callable: The wrapped method with input/output history tracking.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper
#!/usr/bin/env python3
"""
Module for Cache class to interact with Redis and store data.
"""

import redis
import uuid
from typing import Union, Callable, Any
import functools


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called using Redis INCR.
    Uses the method's __qualname__ as the key.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def get(self, key: str, fn: 'Callable[[bytes], Union[str, int, bytes, float]]' = None) -> Union[str, int, bytes, float, None]:
        """
        Retrieve a value from Redis by key and optionally convert it using fn.

        Args:
            key: The Redis key to retrieve.
            fn: Optional callable to convert the bytes value to the desired type.

        Returns:
            The value from Redis, converted if fn is provided, or None if key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Retrieve a string value from Redis by key.

        Args:
            key: The Redis key to retrieve.

        Returns:
            The value decoded as UTF-8 string, or None if key does not exist.
        """
        value = self.get(key, fn=lambda d: d.decode('utf-8'))
        return value

    def get_int(self, key: str) -> int:
        """
        Retrieve an integer value from Redis by key.

        Args:
            key: The Redis key to retrieve.

        Returns:
            The value converted to int, or None if key does not exist.
        """
        value = self.get(key, fn=int)
        return value
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

    @call_history
    @count_calls
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
