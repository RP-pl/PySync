import threading


class ConcurrentList:
    def __init__(self, *args):
        self.list = list(args)
        self.lock = threading.Lock()

    def append(self, item):
        with self.lock:
            self.list.append(item)

    def extend(self, items):
        with self.lock:
            self.list.extend(items)

    def insert(self, index, item):
        with self.lock:
            self.list.insert(index, item)

    def remove(self, item):
        with self.lock:
            self.list.remove(item)

    def pop(self, index=-1):
        with self.lock:
            return self.list.pop(index)

    def clear(self):
        with self.lock:
            self.list.clear()

    def index(self, item, start=0, end=None):
        with self.lock:
            return self.list.index(item, start, end)


    def __getitem__(self, item):
        with self.lock:
            return self.list[item]

    def __setitem__(self, item, value):
        with self.lock:
            self.list[item] = value

    def __delitem__(self, item):
        with self.lock:
            del self.list[item]

    def __iter__(self):
        with self.lock:
            return iter(self.list)

    def __len__(self):
        with self.lock:
            return len(self.list)

    def __contains__(self, item):
        with self.lock:
            return item in self.list

    def __str__(self):
        with self.lock:
            return str(self.list)

    def __repr__(self):
        with self.lock:
            return repr(self.list)
