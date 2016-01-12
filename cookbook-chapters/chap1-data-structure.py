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


def test_itemgetter():
	from operator import itemgetter
	rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
	]
	row_by_fname = sorted(rows, key=itemgetter('fname'))
	row_by_uid = sorted(rows, key=itemgetter('uid'))
	print row_by_fname
	print row_by_uid
	# accept multiple keys
	row_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
	print row_by_lfname
	print min(rows, key=itemgetter('uid'))
	print min(rows, key=lambda r: r['uid'])

def test_attrgetter():
	from operator import attrgetter

	class User(Object):
		def __init__(self, user_id):
			self.user_id = user_id

		def __repr__(self):
			return 'User({})'.format(self.user_id)

	users = [User(23), User(3), User(90)]
	print users
	print sorted(users, key=attrgetter('user_id'))
	print sorted(users, key=lambda u: u.user_id)

# Abandon: no ChainMap in Python2.7
# But it's particularly useful when working with scoped values
# such as variables in a programming language (i.e., globals, locals, etc.)
def test_ChainMap():
	from collections import ChainMap
	a = {'x': 1, 'z': 3}
	b = {'y': 2, 'z': 4}
	c = ChainMap(a, b)
	print (c['x'], c['y'], c['z'])


def main():
	# test_dedupe_with_order()
	# test_itemgetter()
	test_ChainMap()




if __name__=='__main__':
	main()