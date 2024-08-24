#!/usr/bin/python3
"""LFU Caching"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A LRUCache class that define a LRU algorithm to use cache"""

    def __init__(self):
        """Initiliazation"""
        super().__init__()
        self.leastrecent = []

    def put(self, key, item):
        """modify cache data"""
        if key or item is not None:
            cache_value = self.get(key)
            if cache_value is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    keydel = self.leastrecent
                    lendel = len(keydel) - 1
                    del self.cache_data[keydel[lendel]]
                    print("DISCARD: {}".format(self.leastrecent.pop()))
            else:
                del self.cache_data[key]

            if key in self.leastrecent:
                indextodel = self.search_first(self.leastrecent, key)
                self.leastrecent.pop(indextodel)
                self.leastrecent.insert(0, key)
            else:
                self.leastrecent.insert(0, key)

            self.cache_data[key] = item

    def get(self, key):
        """Return value"""
        cache_value = self.cache_data.get(key)

        if cache_value:
            indextodel = self.search_first(self.leastrecent, key)
            self.leastrecent.pop(indextodel)
            self.leastrecent.insert(0, key)

        return cache_value

    @staticmethod
    def search_first(mrulist, key):
        for i in range(0, len(mrulist)):
            if mrulist[i] == key:
                return (i)
        return None
