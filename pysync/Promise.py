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