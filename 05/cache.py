from collections import deque


class LRUCache:
    def __init__(self, limit=20):
        if limit < 1:
            raise ValueError
        self.cache = dict()
        self.queue = deque()
        self.limit = limit

    def get(self, key):
        if key in self.cache:
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.cache[key]
        return None

    def set(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.queue.remove(key)
            self.queue.appendleft(key)
        else:
            if len(self.cache) < self.limit:
                self.cache[key] = value
            else:
                oldest_key = self.queue.pop()
                self.cache.pop(oldest_key)
                self.cache[key] = value
            self.queue.appendleft(key)
