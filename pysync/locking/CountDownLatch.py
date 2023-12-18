import threading


class CountDownLatch:

    def __init__(self, count):
        self.count = count
        self.lock = threading.Condition()

    def countDown(self):
        with self.lock:
            self.count -= 1
            if self.count <= 0:
                self.lock.notifyAll()

    def wait(self):
        with self.lock:
            while self.count > 0:
                self.lock.wait()

    def getCount(self):
        with self.lock:
            return self.count

    def __str__(self):
        return "CountDownLatch(count=%d)" % self.count

    def __repr__(self):
        return self.__str__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass