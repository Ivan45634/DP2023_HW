from collections import deque


class LRUCache:
    def __init__(self, limit=42):
        self.cache = {}
        self.queue = deque()
        self.limit = limit

    def get(self, key):
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        else:
            return None

    def set(self, key, value):
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
        else:
            if len(self.queue) >= self.limit:
                oldest = self.queue.popleft()
                del self.cache[oldest]
            self.queue.append(key)
        self.cache[key] = value
