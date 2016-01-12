#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate
from os import listdir
import re

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

def test_re_sub():
	text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
	# replace 11/27/2012 to 2012-11-27
	print re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

	# use callback to substitute
	datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
	from calendar import month_abbr
	def change_date(m):
		mon_name = month_abbr[int(m.group(1))]
		return '{} {}, {}'.format(mon_name, m.group(2), m.group(3))
	print datepat.sub(change_date, text)

def test_re_ignorecase():
	text = 'UPPER PYTHON, lower python, Mixed Python'
	print re.findall('python', text, flags=re.IGNORECASE)
	# The 'snake' won't match the case of the matched text
	print re.sub('python', 'snake', text, flags=re.IGNORECASE)
	# To fix it
	def matchcase(word):
		def replace(m):
			text = m.group()
			if text.isupper():
				return word.upper()
			elif text.islower():
				return word.lower()
			elif text[0].isupper():
				return word.capitalize()
			else:
				return word
		return replace

	print re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)


def test_shortest_match():
	# match between double quotes
	text = 'Computer says "no." Phone says "yes."'
	str_pat = re.compile(r'\"(.*)\"')
	print str_pat.findall(text)
	str_pat2 = re.compile(r'\"(.*?)\"')
	print str_pat2.findall(text)

def main():
	test_shortest_match()




if __name__=='__main__':
	main()