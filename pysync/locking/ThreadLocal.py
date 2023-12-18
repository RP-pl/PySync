import threading

from pysync.collections.ConcurrentDict import ConcurrentDict


class ThreadLocal:

    def __init__(self):
        self._local = ConcurrentDict()

    def get(self, key):
        return self._local.get(threading.current_thread().ident, {}).get(key, None)

    def set(self, key, value):
        self._local.setdefault(threading.current_thread().ident, {})[key] = value