#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from collections import deque, Iterable
import itertools
from itertools import chain
import heapq
import sys

def test_generator():
	def frange(start, stop, increment):
		x = start
		while x < stop:
			yield x
			x += increment
	for n in frange(0, 4, 0.5):
		print(n)
	print(list(frange(0, 1, 0.125)))

class Node(object):
	def __init__(self, value):
		self._value = value
		self._children = []

	def __repr__(self):
		return 'Node({!r})'.format(self._value)

	def add_child(self, node):
		self._children.append(node)

	def __iter__(self):
		return iter(self._children)

	def depth_first(self):
		yield self
		for c in self:
			yield from c.depth_first()

def test_iterator_protocol():
	root = Node(0)
	child1 = Node(1)
	child2 = Node(2)
	root.add_child(child1)
	root.add_child(child2)
	child1.add_child(Node(3))
	child1.add_child(Node(4))
	child2.add_child(Node(5))

	for ch in root.depth_first():
		print(ch)


def test_custom_reverse():
	class Countdown:
		def __init__(self, start):
			self.start = start

		def __iter__(self):
			n = self.start
			while n > 0:
				yield n
				n -= 1

		def __reversed__(self):
			n = 1
			while n <= self.start:
				yield n
				n += 1

	for x in reversed(Countdown(4)):
		print(x)

def test_generator_with_extra_state():
	'''Use a class definition and define the generator in __iter__() method'''
	class linehistory:
		def __init__(self, lines, histlen=3):
			self.lines = lines
			self.history = deque(maxlen=histlen)

		def __iter__(self):
			for lineno, line in enumerate(self.lines, 1):
				self.history.append((lineno, line))
				yield line

		def clear(self):
			self.history.clear()

	with open('somefile.txt') as f:
		lines = linehistory(f)
		for line in lines:
			if 'python' in line:
				for lineno, hline in lines.history:
					print('{}:{}'.format(lineno, hline), end='')


def test_slice_iterator():
	def count(n):
		while True:
			yield n
			n += 1

	c = count(0)
	for x in itertools.islice(c, 10, 20):
		print(x)

def test_enumerate():
	# second argu is the start counter
	data = [(1,2), (3, 4), (5, 6), (7, 8)]
	for n, (x, y) in enumerate(data, 1):
		print(n, x, y)
	# or
	for n, d in enumerate(data, 1):
		print(n, d)
	# Wrong
	# for n, x, y in enumerate(data, 1):
	 	# pass

def test_itertool_chain():
	a = [1, 2, 3, 4]
	b = ['x', 'y', 'z']
	for x in chain(a, b):
		print(x)

	# or
	active_items = set()
	inactive_items = set()
	for item in chain(active_items, inactive_items):
		pass

def test_flatten():
	def flatten(items, ignore_types=(str, bytes)):
		for x in items:
			if isinstance(x, Iterable) and not isinstance(x, ignore_types):
				yield from flatten(x)
			else:
				yield x
	items = [1, 2, [3, 4, [5, 6], 7], 8]
	for x in flatten(items):
		print(x)


def test_merge_sorted_iterables():
	'''
	Even work with very long sequences with very litter overhead.
	Required sorted sequences ahead.
	'''
	with open('sorted_file_1', 'rt') as file1, \
		 open('sorted_file_2', 'rt') as file2, \
		 open('merged_file', 'wt') as outf:

		for line in heapq.merge(file1, file2):
			outf.write(line)


def test_replace_infinite_while_loop():
	'''
	iter() also accepts a zero-argument callable and 
	sentinel (terminating) value
	'''
	f = open('/etc/passwd')
	for chunk in iter(lambda: f.read(10), ''):  # chunksize = 10
		n = sys.stdout.write(chunk)

def main():
	test_replace_infinite_while_loop()




if __name__=='__main__':
	main()