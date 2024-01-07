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

    def get(self, ident):
        """
        Returns the value of the given parameter for the given identifier.
        :param ident: key to look up.
        :return:
        """
        with self._lock:
            return self._dict.get(ident, None)

    def set(self, ident, value):
        """
        Sets the value of the given parameter for the given identifier.
        :param ident: key to set.
        :param value: value to set.
        :return:
        """
        with self._lock:
            if ident not in self._dict:
                self._dict[ident] = {}
            self._dict[ident] = value

    def remove(self, ident):
        """
        Removes the given identifier from the dictionary.
        :param ident: key to remove.
        :return:
        """
        with self._lock:
            if ident in self._dict:
                    del self._dict[ident]

    def setdefault(self, ident, param):
        """
        Returns the value of the given parameter for the given identifier.
        :param ident: key to look up.
        :param param: parameter to look up.
        :return:
        """
        with self._lock:
            self._dict.setdefault(ident, param)
