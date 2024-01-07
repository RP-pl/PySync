import threading


class CountDownLatch:
    """
        A synchronization aid that allows one or more threads to wait until a set of operations being performed
        in other threads completes.
        A CountDownLatch is initialized with a given count.
        The await methods block until the current count reaches zero due to invocations of the countDown() method,
        after which all waiting threads are released and any subsequent invocations of await return immediately.
        This is a one-shot phenomenon -- the count cannot be reset.
    """

    def __init__(self, count):
        self.count = count
        self.lock = threading.Condition()

    def countDown(self):
        """
            Decrements the count of the latch, releasing all waiting threads if the count reaches zero.
        """
        with self.lock:
            self.count -= 1
            if self.count <= 0:
                self.lock.notifyAll()

    def wait(self):
        """
            Causes the current thread to wait until the latch has counted down to zero, unless the thread is interrupted.
        """
        with self.lock:
            while self.count > 0:
                self.lock.wait()

    def getCount(self):
        """
            Returns how many times countDown() must be invoked before threads can pass through await.
        """
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