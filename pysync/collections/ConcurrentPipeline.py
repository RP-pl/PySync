from queue import Queue
from threading import Semaphore


class ConcurrentPipeline:

    def __init__(self, length):
        self.length = length
        self._semaphore = Semaphore(length)
        self._queue = Queue()

    def put(self, item):
        self._semaphore.acquire(blocking=True)
        self._queue.put(item)

    def get(self):
        item = self._queue.get()
        self._semaphore.release()
        return item

    def clear(self):
        self._queue.queue.clear()
        self._semaphore = Semaphore(self.length)

    def __iter__(self):
        return self

    def __next__(self):
        return self.get()

    def __len__(self):
        return self.length