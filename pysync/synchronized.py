from threading import Lock
from typing import Callable
from functools import wraps


class synchronized:
    """
        Decorator that synchronizes method and function calls with a given lock.
        The lock is passed as the first argument to the decorated function.
        This decorator supports any lock that implements the context manager protocol.
        Example:
            >>> from threading import RLock
            >>> lock = RLock()
            >>> @synchronized(lock)
            ... def foo():
            ...     pass
            >>> foo()
    """

    def __init__(self, lock: Lock):
        self.lock = lock


    def __call__(self, func: Callable[..., any]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with self.lock:
                return func(*args, **kwargs)
        return wrapper