import unittest

from pysync.locking.ThreadLocal import ThreadLocal


class ThreadLocalTest(unittest.TestCase):

    def test(self):
        tl = ThreadLocal()
        from threading import Thread
        from time import sleep
        def worker(i):
            sleep(0.1)
            tl.set("a",i)
            self.assertEqual(tl.get("a"), i)

        threads = [Thread(target=worker, args=(i,)) for i in range(2,10)]
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
        tl.set("a",1)
        self.assertEqual(tl.get("a"), 1)