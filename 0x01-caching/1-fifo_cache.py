#!/usr/bin/python3
"""BaseCache module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache define a FIFO algorithm to use cache"""

    def __init__(self):
        """ Initiliazation"""
        super().__init__()

    def put(self, key, item):
        """modify cache data"""
        if key or item is not None:
            cache_value = self.get(key)
            if cache_value is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydel = list(self.cache_data.keys())[0]
                    del self.cache_data[keydel]
                    print("DISCARD: {}".format(keydel))
            self.cache_data[key] = item

    def get(self, key):
        """modify cache data"""
        cache_value = self.cache_data.get(key)
        return cache_value
