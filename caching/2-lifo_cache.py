#!/usr/bin/env python3
""" LIFOCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system
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

        # If key already exists, remove it from order list
        if key in self.cache_data:
            self.order.remove(key)
        else:
            # Check if cache is full
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove last item (LIFO)
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))

        # Add/update item
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
