def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function, including the number of calls, inputs, and outputs.

    Args:
        method: The method whose call history to display.

    Prints:
        The number of times the method was called, and the list of inputs and outputs for each call.
    """
    if not hasattr(method, "__self__") or not hasattr(method, "__qualname__"):
        return
    redis_client = method.__self__._redis
    qualname = method.__qualname__
    inputs = redis_client.lrange(f"{qualname}:inputs", 0, -1)
    outputs = redis_client.lrange(f"{qualname}:outputs", 0, -1)
    call_count = redis_client.get(qualname)
    try:
        call_count = int(call_count)
    except (TypeError, ValueError):
        call_count = 0
    print(f"{qualname} was called {call_count} times:")
    for input_bytes, output_bytes in zip(inputs, outputs):
        input_str = input_bytes.decode('utf-8')
        output_str = output_bytes.decode('utf-8')
        print(f"{qualname}(*{input_str}) -> {output_str}")
#!/usr/bin/env python3
"""
Module for Cache class to interact with Redis and store data in a Redis database.
Provides decorators for counting method calls and storing call history (inputs and outputs).
"""

import redis
import uuid
from typing import Union, Callable, Any
import functools

def call_history(method: Callable) -> Callable:
    """
    Decorator that stores the history of inputs and outputs for a method in Redis lists.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper
def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function, including the number of calls, inputs, and outputs.
    """
    if not hasattr(method, "__self__") or not hasattr(method, "__qualname__"):
        return
    redis_client = method.__self__._redis
    qualname = method.__qualname__
    inputs = redis_client.lrange(f"{qualname}:inputs", 0, -1)
    outputs = redis_client.lrange(f"{qualname}:outputs", 0, -1)
    call_count = redis_client.get(qualname)
    try:
        call_count = int(call_count)
    except (TypeError, ValueError):
        call_count = 0
    print(f"{qualname} was called {call_count} times:")
    for input_bytes, output_bytes in zip(inputs, outputs):
        input_str = input_bytes.decode('utf-8')
        output_str = output_bytes.decode('utf-8')
        print(f"{qualname}(*{input_str}) -> {output_str}")

import redis
import uuid
from typing import Union, Callable, Any
import functools


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called using Redis INCR.
    Uses the method's __qualname__ as the key.

    Args:
        method: The method to decorate.

    Returns:
        Callable: The wrapped method with call counting.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        Wrapper function that increments the call count in Redis and calls the method.

        Args:
            self: The instance of the class.
            *args: Arguments passed to the method.
            **kwargs: Keyword arguments passed to the method.

        Returns:
            Any: The output of the original method.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


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

    def get(self, key: str, fn: Callable[[bytes], Union[str, int, bytes, float]] = None) -> Union[str, int, bytes, float, None]:
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

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve a string value from Redis by key.

        Args:
            key: The Redis key to retrieve.

        Returns:
            The value decoded as UTF-8 string, or None if key does not exist.
        """
        value = self.get(key, fn=lambda d: d.decode('utf-8'))
        return value

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve an integer value from Redis by key.

        Args:
            key: The Redis key to retrieve.

        Returns:
            The value converted to int, or None if key does not exist.
        """
        value = self.get(key, fn=int)
        return value
