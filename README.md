# PySync

## Description

PySync is a library extending the functionality of pythons built-in threading capabilities.
It extends capabilities of built-in synchronization by adding higher level synchronization primitives such as reentrant locks, barriers and latches.
It also adds another layer of abstraction by providing Promise API for asynchronous programming.

## Functionalities
### pysync
* #### locking
  * **CountDownLatch** - a synchronization primitive that allows one or more threads to wait until a set of operations being performed in other threads completes.
  * **ReentrantLock** - a synchronization primitive that may be acquired multiple times by the same thread.
  * **CycleBarrier** - a synchronization primitive that allows a set of threads to all wait for each other to reach a common barrier point.
  * **RWLock** - a synchronization primitive that solves the readers-writers problem.
  * **ThreadLocal** - a synchronization primitive that allows to store data local to a thread.
* #### meta
  * **synchronized** - a decorator that allows to synchronize a method or a function.
  * **Synchronized** - a metaclass that allows to synchronize all methods of a class.

* #### collections
    * **ConcurrentPipeline** - thread-safe data structure that adds elements up to given capacity and then blocks until some elements are removed.
    * **ConcurrentDict** - thread-safe dictionary.
    * **ConcurrentList** - thread-safe list.
    * **ConcurrentStack** - thread-safe stack.

* **Promise** - a synchronization primitive that represents a value that may be available in the future.
