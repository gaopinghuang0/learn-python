#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from queue import Queue
from functools import partial, wraps
import sys
from timeit import timeit


# call back function
def apply_async(func, args, *, callback):
    result = func(*args)

    # Invoke the callback with the result
    callback(result)

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y


# one way to carry extra information in a callback
class ResultHandler(object):
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result)) 

# use closure to capture state
def make_handler():
    sequence = 0
    def handler(result):
        # nonlocal declaration is used to indicate that 
        # the sequence variable is being modified from within the callback
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

# use a coroutine to accomplish the same thing
def make_hander_2():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


# use partial function to carry state
class SequenceNo(object):
    def __init__(self):
        self.sequence = 0

def handler3(result, seq):
    seq.sequence += 1
    print('[{}] Got: {}'.format(seq.sequence, result))

class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args

def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper

@inlined_async
def test_inlined_async():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')


# Access variables defined inside a closure
def sample():
    n = 0
    # closure function
    def func():
        print('n=', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func

def test_access_varible_inside():
    f = sample()
    f()
    f.set_n(10)
    f()
    print(f.get_n())


# emulate instances of a class
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # Update instance dictionary with callables
        self.__dict__.update((key,value) for key, value in locals.items()
            if callable(value))

    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()

# Example use
def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

# A normal class definition
class Stack2:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

def test_emulate_class_instance():
    s = Stack()
    print(s)
    s.push(10)
    s.push(20)
    s.push('hello')
    print(len(s))
    print(s.pop())

    # Compare run-time of emulated class to normal class
    # Test involving closures
    t1 = timeit('s.push(1);s.pop()', 'from __main__ import Stack; s=Stack()')
    print(t1)
    # Test involving a class
    t2 = timeit('s.push(1);s.pop()', 'from __main__ import Stack2; s=Stack2()')
    print(t2)
    # timeit('s.push(1);s.pop()', setup='s=s')

def main():
    apply_async(add, (2,3), callback=print_result)
    apply_async(add, ('hello', 'world'), callback=print_result)

    r = ResultHandler()
    apply_async(add, (2, 3), callback=r.handler)
    apply_async(add, ('hello', 'world'), callback=r.handler)

    handler = make_handler()
    apply_async(add, (2, 3), callback=handler)
    apply_async(add, ('hello', 'world'), callback=handler)  

    handler2 = make_hander_2()
    next(handler2)
    apply_async(add, (2, 3), callback=handler2.send)
    apply_async(add, ('hello', 'world'), callback=handler2.send)        

    seq = SequenceNo()
    apply_async(add, (2, 3), callback=partial(handler3, seq=seq))
    apply_async(add, ('hello', 'world'), callback=partial(handler3, seq=seq))   

    test_inlined_async()

    test_access_varible_inside()

    test_emulate_class_instance()


if __name__=='__main__':
    main()