#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate
from os import listdir

def test_endswith():
	filenames = listdir('.')
	if any(name.endswith(('.c', '.h')) for name in filenames):
		print 'some C lang files'
	elif any(name.endswith(('.py', '.pyc')) for name in filenames):
		print 'some Python files'


def test_fnmatch():
	from fnmatch import fnmatch, fnmatchcase
	print fnmatch('foo.txt', '*.txt')
	print fnmatch('foo.txt', '?oo.txt')
	print fnmatch('Dat45.csv', 'Dat[0-9]*')
	# case-sensitivity
	print fnmatch('foo.txt', '*.TXT')
	print fnmatchcase('foo.txt', '*.TXT')



def main():
	test_fnmatch()




if __name__=='__main__':
	main()