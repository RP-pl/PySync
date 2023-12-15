import threading

from pysync import synchronized


class Synchronized(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value):
                attrs[attr_name] = synchronized(threading.Lock())(attr_value)
        return super(Synchronized, cls).__new__(cls, name, bases, attrs)