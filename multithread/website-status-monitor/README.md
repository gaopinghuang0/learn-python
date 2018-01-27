## Website status monitor
The purpose of these apps is to notify you when your website is down so that you can quickly take action. 

### Based on the tutorial:
[Introduction to Parallel and Concurrent Programming in Python](https://code.tutsplus.com/articles/introduction-to-parallel-and-concurrent-programming-in-python--cms-28612)

### Different approaches
There are several approaches for the same purpose: `serial`, `threading`, `concurrent.futures`, `multiprocessing`, `gevent`, and `celery`. Since the `celery` is very different from the other ones, I did not include its example.

### Conclusion from the tutorial
* There are several paradigms that help us achieve high-performance computing in Python.
* For the multi-threaded paradigm, we have the `threading` and `concurrent.futures` libraries.
* `multiprocessing` provides a very similar interface to `threading` but for processes rather than threads.
* Remember that processes achieve true parallelism, but they are more expensive to create.
* Remember that a process can have more threads running inside it.
* Do not mistake parallel for concurrent. Remember that only the parallel approach takes advantage of multi-core processors, whereas concurrent programming intelligently schedules tasks so that waiting on long-running operations is done while in parallel doing actual computation.