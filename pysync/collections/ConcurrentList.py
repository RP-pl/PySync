import threading


class ConcurrentList:
    def __init__(self, *args):
        self.list = list(args)
        self.lock = threading.Lock()

    def append(self, item):
        """
        Appends an item to the list.
        :param item: An item to append to the list.
        :return:
        """
        with self.lock:
            self.list.append(item)

    def extend(self, items):
        """
        Extends the list with the given items.
        :param items: A list of items to extend the list with.
        :return:
        """
        with self.lock:
            self.list.extend(items)

    def insert(self, index, item):
        """
        Inserts an item at the given index.
        :param index: index to insert the item at.
        :param item: item to insert.
        :return:
        """
        with self.lock:
            self.list.insert(index, item)

    def remove(self, item):
        """
        Removes the first occurrence of the given item from the list.
        :param item: item to be removed.
        :return:
        """
        with self.lock:
            self.list.remove(item)

    def pop(self, index=-1):
        """
        Removes and returns the item at the given index.
        :param index: index of the item to be removed.
        :return: item at the given index.
        """
        with self.lock:
            return self.list.pop(index)

    def clear(self):
        """
        Removes all items from the list.
        :return:
        """
        with self.lock:
            self.list.clear()

    def index(self, item, start=0, end=None):
        """
        Returns the index of the first occurrence of the given item in the list.
        :param item: item to search for.
        :param start: index to start searching from.
        :param end: index to stop searching at.
        :return: index of the first occurrence of the given item in the list.
        """
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
