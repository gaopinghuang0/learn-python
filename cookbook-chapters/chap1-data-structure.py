#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate
from collections import Counter

def dedupe_with_order(items, key=None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)

def test_dedupe_with_order():
	a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 2}]
	print list(dedupe_with_order(a, key=lambda d: (d['x'], d['y'])))
	print list(dedupe_with_order(a, key=lambda d: d['x']))





def main():
	test_dedupe_with_order()




if __name__=='__main__':
	main()