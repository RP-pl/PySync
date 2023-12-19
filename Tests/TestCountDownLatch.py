import unittest

from pysync.locking.CountDownLatch import CountDownLatch


class TestLatch(unittest.TestCase):

    def test(self):

        from threading import Thread
        from time import sleep


        latch = CountDownLatch(3)

        def worker():
            sleep(0.1)
            latch.countDown()

        threads = [Thread(target=worker) for _ in range(3)]
        for thread in threads:
            thread.start()

        latch.wait()

        for thread in threads:
            thread.join()

        self.assertEqual(latch.count, 0)