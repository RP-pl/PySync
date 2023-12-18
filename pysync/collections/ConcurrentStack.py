from collections.abc import Collection
from threading import Lock
class ConcurrentStack(Collection):

    def __init__(self, *args, **kwargs):
        self._stack = list(*args, **kwargs)
        self._lock = Lock()

    def __contains__(self, x):
        self._lock.acquire()
        try:
            return x in self._stack
        finally:
            self._lock.release()

    def __iter__(self):
        try:
            self._lock.acquire()
            return _ConcurrentStackIterator(self._stack)
        finally:
            self._lock.release()

    def __len__(self):
        self._lock.acquire()
        try:
            return len(self._stack)
        finally:
            self._lock.release()

    def push(self, x):
        self._lock.acquire()
        try:
            self._stack.append(x)
        finally:
            self._lock.release()

    def pop(self):
        self._lock.acquire()
        try:
            element = self._stack[-1]
            del self._stack[-1]
            return element
        finally:
            self._lock.release()

    def peek(self):
        self._lock.acquire()
        try:
            return self._stack[-1]
        finally:
            self._lock.release()

    def clear(self):
        self._lock.acquire()
        try:
            self._stack.clear()
        finally:
            self._lock.release()

    def __repr__(self):
        self._lock.acquire()
        try:
            return repr(self._stack)
        finally:
            self._lock.release()

    def __str__(self):
        self._lock.acquire()
        try:
            return str(self._stack)
        finally:
            self._lock.release()

    def __getitem__(self, index):
        raise NotImplementedError("ConcurrentStack does not support __getitem__")

    def __setitem__(self, index, value):
        raise NotImplementedError("ConcurrentStack does not support __setitem__")

class _ConcurrentStackIterator:

    def __init__(self, stack):
        self._stack = stack
        self._index = 0

    def __next__(self):
        if self._index >= len(self._stack):
            raise StopIteration
        self._index += 1
        return self._stack[self._index - 1]