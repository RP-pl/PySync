import threading

from .sync_decorator import synchronized


def _synchronize_set_attr(method):
    def set_attr(self, name, value):
        if callable(value):
            value = synchronized(threading.Lock())(value)
        method(self, name, value)
    return set_attr


class Synchronized(type):
    """
        A metaclass that wraps all methods of a class with the synchronized decorator.
        This metaclass also wraps the __setattr__ method of the class to synchronize attribute setting.
    """
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value):
                attrs[attr_name] = synchronized(threading.Lock())(attr_value)

        cls.__setattr__ = _synchronize_set_attr(cls.__setattr__)
        return super(Synchronized, cls).__new__(cls, name, bases, attrs)
