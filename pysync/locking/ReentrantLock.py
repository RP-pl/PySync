import threading


class ReentrantLock:

    """
        A reentrant lock that can be acquired multiple times by the same thread.
        This lock is not fair, meaning that there is no guarantee that the first thread that requests the lock will be the first thread to acquire it.
    """

    def __init__(self):
        self._lock = threading.Lock()
        self._owner = None
        self._count = 0

    def acquire(self):
        """
            Acquires the lock.
            If the lock is already held by another thread, the current thread will block until the lock is released.
            If the lock is already held by the current thread, the lock will be acquired again.
        """
        current_thread = threading.current_thread()
        if self._owner == current_thread:
            self._count += 1
            return
        self._lock.acquire()
        self._owner = current_thread
        self._count = 1

    def release(self):
        """
            Releases the lock.
            If the lock is not held by the current thread, a RuntimeError will be raised.
            If the lock is held multiple times by the current thread, the lock will be released once.
        """
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