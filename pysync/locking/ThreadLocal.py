import threading

from ..collections.ConcurrentDict import ConcurrentDict


class ThreadLocal:
    """
         A thread local object that stores a dictionary of key-value pairs for each thread.
         The key-value pairs can be accessed using the get and set methods.
    """

    def __init__(self):
        self._local = ConcurrentDict()

    def get(self, key):
        return self._local.get(threading.current_thread().ident, {}).get(key, None)

    def set(self, key, value):
        self._local.setdefault(threading.current_thread().ident, {})[key] = value