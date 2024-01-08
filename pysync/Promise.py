from concurrent.futures import ThreadPoolExecutor

from pysync.collections import ConcurrentPipeline


def _run_executor_loop(value, pipleline):
    while True:
        func = pipleline.get()
        if func is None:
            break
        else:
            value = func(value)
    return value


class Promise:
    """
        A promise is a wrapper around a value that allows for asynchronous execution of functions on that value.
        The value is passed to the first function in the pipeline, and the result of that function is passed to the
        second function in the pipeline, and so on. The result of the last function in the pipeline is the value of
        the promise. The pipeline is executed asynchronously in a thread pool.
    """
    def __init__(self, value=None, pipeline_size=1024):
        self._executor = ThreadPoolExecutor(max_workers=1)
        self._value = value
        self._pipeline = ConcurrentPipeline(pipeline_size)
        self._future = self._executor.submit(_run_executor_loop, value, self._pipeline)
        self._done = False

    def then(self, func):
        self._pipeline.put(func)
        return self

    def get(self):
        if not self._done:
            self._done = True
            self._pipeline.put(None)
            self._value = self._future.result()
        return self._value

    def done(self):
        """
            Returns true if the promise has been fulfilled.
        :return: Boolean
        """
        return self._done
    @staticmethod
    def all(*promises):
        """
            Returns a promise that is fulfilled when all of the given promises are fulfilled.
        :param promises: promises to wait for
        :return: Promise containing the values of the given promises
        """
        return Promise([p.get() for p in promises])

    @staticmethod
    def any(*promises):
        """
            Returns a promise that is fulfilled when any of the given promises are fulfilled.
            :param promises: promises to wait for
            :return: Promise containing the value of the first promise to be fulfilled
        """
        while True:
            for p in promises:
                if p.done():
                    return Promise(p.get())


    def run_after_either(self, other, func):
        """
            Returns a promise that is fulfilled when either of the given promises are fulfilled.
        :param other: other promise
        :param func: function to run on the value of the first promise to be fulfilled
        :return: A promise containing the result of the given function
        """
        return Promise.any(self, other).then(func)

    def run_after_all(self, other, func):
        """
            Returns a promise that is fulfilled when both of the given promises are fulfilled.
            :param other: other promises
            :param func: function to run on the values of the given promises
            :return: A promise containing the result of the given function
        """
        return Promise.all(self, other).then(func)