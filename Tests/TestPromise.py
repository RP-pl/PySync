import time
import unittest


class TestPromise(unittest.TestCase):

        def test(self):

            from pysync import Promise

            arr = []
            promise = Promise(1)

            def first(value):
                arr.append(value+1)
                return value+1

            def second(value):
                time.sleep(0.2)
                arr.append(value+1)
                return value+1

            promise.then(first)
            promise.then(second)
            time.sleep(0.1)
            arr.append(0)



            result = promise.get()

            self.assertEqual(result, 3)
            self.assertEqual(arr, [2, 0, 3])