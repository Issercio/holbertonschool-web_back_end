# 0x0B. Redis basic

>This project demonstrates how to use Redis as a key-value store in Python, including storing, retrieving, and managing data with type annotations and full documentation.

## Features
- Connects to a Redis server using `redis-py`
- Stores data of various types (str, bytes, int, float) with random keys
- Demonstrates type annotations and Python docstrings for all modules, classes, and methods
- Flushes the Redis database on initialization for a clean state

## Files
- `exercise.py`: Contains the `Cache` class for storing and retrieving data in Redis.
- `main.py`: Example usage of the `Cache` class (see below).

## Requirements
- Python 3.9+
- `redis` Python package (`pip install redis`)
- Redis server (can be run in a container)

## Getting Started
1. **Start your Redis server:**
   ```bash
   service redis-server start
   ```
   Or, if using Docker:
   ```bash
   docker run --name redis-basic -p 6379:6379 -d redis:alpine
   ```

2. **Install dependencies:**
   ```bash
   pip install redis
   ```

3. **Run the main file:**
   ```bash
   python3 main.py
   ```

## Example Usage
```python
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
```

**Expected output:**
```
3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
b'hello'
```

## Project Structure
- `exercise.py`: Main module with the `Cache` class
- `main.py`: Example/test script
- `README.md`: Project documentation
