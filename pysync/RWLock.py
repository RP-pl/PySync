from threading import Lock


class RWLock:

    def __init__(self):
        self._readCount = 0
        self._writeLock = Lock()
        self._readLock = Lock()

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