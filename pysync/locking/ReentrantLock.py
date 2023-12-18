import threading


class ReentrantLock:

    def __init__(self):
        self._lock = threading.Lock()
        self._owner = None
        self._count = 0

    def acquire(self):
        current_thread = threading.current_thread()
        if self._owner == current_thread:
            self._count += 1
            return
        self._lock.acquire()
        self._owner = current_thread
        self._count = 1

    def release(self):
        if self._count == 0:
            raise RuntimeError("Cannot release a lock that is not locked")
        self._count -= 1
        if self._count == 0:
            self._owner = None
            self._lock.release()

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.release()