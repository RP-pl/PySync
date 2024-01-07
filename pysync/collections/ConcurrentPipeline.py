from queue import Queue
from threading import Semaphore


class ConcurrentPipeline:

    def __init__(self, length):
        self.length = length
        self._semaphore = Semaphore(length)
        self._queue = Queue()

    def put(self, item):
        """
        Puts an item into the pipeline.
        If the pipeline is full, this method will block until an item is removed from the pipeline.
        :type item: any
        :param item: any item to be put into the pipeline
        """
        self._semaphore.acquire(blocking=True)
        self._queue.put(item)

    def get(self):
        """
            Gets an item from the pipeline.
            If the pipeline is empty, this method will block until an item is put into the pipeline.
        :return:
        """
        item = self._queue.get()
        self._semaphore.release()
        return item

    def clear(self):
        """
            Clears the pipeline.
            This method will block until all items are removed from the pipeline.
        """
        self._queue.queue.clear()
        self._semaphore = Semaphore(self.length)

    def __iter__(self):
        return self

    def __next__(self):
        return self.get()

    def __len__(self):
        return self.length