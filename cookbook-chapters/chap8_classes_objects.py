#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial
import math

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

def test_custom_format():
    d = Date(2012, 12, 21)
    print(format(d))

    print(format(d, 'mdy'))

    print('The date is {:ymd}'.format(d))
    print('The date is {:mdy}'.format(d))


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()

def test_lazy_connect():
    conn = LazyConnection(('www.python.org', 80))
    with conn as s1:
        pass
        with conn as s2:
            pass

# create managed attributes
class Person:
    def __init__(self, first_name):
        # Here, use first_name instead of _first_name is because
        # when init, the type check will also be applied. If use
        # _first_name, the type check will be bypassed
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

def test_manage_attribute():
    b = Person(42)
    a = Person('Guido')
    print(a.first_name)
    a.first_name = 42
    del a.first_name

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
    
def test_define_computed_attributes():
    c = Circle(4.0)
    print(c.radius)
    print(c.area)  # Notice lack of ()
    print(c.perimeter)  # Notice lack of ()

def main():
    test_custom_format()

    # test_manage_attribute()

    test_define_computed_attributes()




if __name__=='__main__':
    main()