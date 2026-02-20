#!/usr/bin/env python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a basic caching system with no limit
    """

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key: the key for the cache item
            item: the value to store in cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        Args:
            key: the key to retrieve from cache
        Returns:
            The value associated with key, or None if not found
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
