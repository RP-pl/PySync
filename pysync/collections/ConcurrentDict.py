#TODO: Implement a concurrent dictionary

from pysync.locking.ReentrantLock import ReentrantLock


class ConcurrentDict:

    def __init__(self):
        self._dict = {}
        self._lock = ReentrantLock()

    def __getitem__(self, key):
        with self._lock:
            return self._dict[key]

    def __setitem__(self, key, value):
        with self._lock:
            self._dict[key] = value

    def __delitem__(self, key):
        with self._lock:
            del self._dict[key]

    def __contains__(self, key):
        with self._lock:
            return key in self._dict

    def __len__(self):
        with self._lock:
            return len(self._dict)

    def __iter__(self):
        with self._lock:
            return iter(self._dict)

    def __str__(self):
        with self._lock:
            return str(self._dict)

    def __repr__(self):
        with self._lock:
            return repr(self._dict)

    def get(self, ident, param):
        with self._lock:
            return self._dict.get(ident, {}).get(param, None)

    def set(self, ident, param, value):
        with self._lock:
            if ident not in self._dict:
                self._dict[ident] = {}
            self._dict[ident][param] = value

    def remove(self, ident, param):
        with self._lock:
            if ident in self._dict:
                if param in self._dict[ident]:
                    del self._dict[ident][param]
                    if len(self._dict[ident]) == 0:
                        del self._dict[ident]

    def remove_all(self, ident):
        with self._lock:
            if ident in self._dict:
                del self._dict[ident]

    def get_all(self, ident):
        with self._lock:
            return self._dict.get(ident, {})

    def setdefault(self, ident, param):
        with self._lock:
            if ident not in self._dict:
                self._dict[ident] = {}
            if param not in self._dict[ident]:
                self._dict[ident][param] = None
            return self._dict[ident][param]
