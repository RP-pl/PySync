from pysync.locking.ReentrantLock import ReentrantLock


class RWLock:
    """
        A read-write lock implementation.
        This lock allows multiple readers to acquire the lock at the same time, but only one writer.
        This lock is reentrant, meaning that a thread can acquire the lock multiple times.
        This lock is not fair, meaning that there is no guarantee that the first thread that requests the lock will be the first thread to acquire it.
    """

    def __init__(self):
        self._readCount = 0
        self._writeLock = ReentrantLock()
        self._readLock = ReentrantLock()

    def acquire_read(self):
        self._readLock.acquire()
        self._readCount += 1
        if self._readCount == 1:
            self._writeLock.acquire()
        self._readLock.release()

    def release_read(self):
        self._readLock.acquire()
        self._readCount -= 1
        if self._readCount == 0:
            self._writeLock.release()
        self._readLock.release()

    def acquire_write(self):
        self._writeLock.acquire()

    def release_write(self):
        self._writeLock.release()

    def __enter__(self):
        self.acquire_write()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.release_write()