import logging
import argparse
from collections import deque


class CustomFilter(logging.Filter):
    """
    Отбрасывает записи с четным числом слов
    """
    def filter(self, record):
        return len(record.getMessage().split()) % 2 != 0


logger = logging.getLogger(__name__)


class LRUCache:
    def __init__(self, limit=42):
        self.cache = {}
        self.queue = deque()
        self.limit = limit
        logger.debug("LRUCache initialized with limit=%d", self.limit)

    def get(self, key):
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            logger.info("Key %s found in cache", key)
            return self.cache[key]
        else:
            logger.info("Key %s not found in cache", key)
            return None

    def set(self, key, value):
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
            logger.info("Key %s updated in cache", key)
        else:
            if len(self.queue) >= self.limit:
                oldest = self.queue.popleft()
                del self.cache[oldest]
                logger.warning("Cache capacity reached, key %s removed from cache", oldest)
            self.queue.append(key)
            logger.debug("Key %s added to cache", key)
        self.cache[key] = value
        logger.info("Key %s set with value %s", key, value)


def main():
    parser = argparse.ArgumentParser(description="LRUCache with logging")
    parser.add_argument("-s", action="store_true", help="Log to stdout")
    parser.add_argument("-f", action="store_true", help="Apply custom filter")
    args = parser.parse_args()

    log_handlers = [logging.FileHandler("cache.log")]
    if args.s:
        log_handlers.append(logging.StreamHandler())

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', handlers=log_handlers)

    if args.f:
        custom_filter = CustomFilter()
        for handler in logging.getLogger().handlers:
            handler.addFilter(custom_filter)

    cache = LRUCache(limit=2)
    cache.set('x', 1)
    cache.get('x')
    cache.get('y')
    cache.set('y', 2)
    cache.set('z', 3)
    cache.set('w', 4)


if __name__ == "__main__":
    main()
