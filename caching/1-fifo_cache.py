#!/usr/bin/env python3
""" FIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key: the key for the cache item
            item: the value to store in cache
        """
        if key is None or item is None:
            return

        # If key already exists, just update the value
        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            # Check if cache is full
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove first item (FIFO)
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))

            # Add new item
            self.cache_data[key] = item
            self.order.append(key)

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
