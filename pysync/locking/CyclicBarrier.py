from pysync.locking import CountDownLatch, ReentrantLock


class CyclicBarrier:
    """
    A synchronization aid that allows a set of threads to all wait for each other to reach a common barrier point.
    CyclicBarriers are useful in programs involving a fixed sized party of threads that must occasionally wait for each other.
    The barrier is called cyclic because it can be re-used after the waiting threads are released.
    """

    def __init__(self, parties):
        self.parties = parties
        self.count = 0
        self.latch = CountDownLatch(parties)
        self._latch_lock = ReentrantLock()

    def wait(self):
        """
        Waits until all parties have invoked wait on this barrier.
        :return:
        """
        self.latch.wait()

    def countDown(self):
        """
        Waits until all parties have invoked wait on this barrier.
        :return:
        """
        self.latch.countDown()
        with self._latch_lock:
            if self.latch.getCount() == 0:
                self.latch = CountDownLatch(self.parties)


    def __str__(self):
        return "CyclicBarrier(parties=%d)" % self.parties

    def __repr__(self):
        return self.__str__()

    def __enter__(self):
        self.countDown()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def getParties(self):
        """
        Returns the number of parties required to trip this barrier.
        :return:
        """
        return self.parties

    def getCount(self):
        """
            Returns how many times countDown() must be invoked before threads can pass through await.
        :return:
        """
        return self.latch.getCount()