#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate
from os import listdir
from collections import namedtuple
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


def test_multiline_match():
	comment = re.compile(r'/\*((?:.|\n)*?)\*/')
	text2 = '''/* this is a 
			 multiline comment */
			 '''
	print comment.findall(text2)
	# or
	comment2 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
	print comment2.findall(text2)

def test_strip():
	s = '     hello world   \n'
	print s.strip()
	print s.lstrip()
	print s.rstrip()

	s = '----hello======'
	print s.lstrip('-')
	print s.strip('-=')


def test_translate():
	s = 'pýtĥöñ\fis\tawesome\r\n'
	print s
	remap = {
		ord('\t'): ' ',
		ord('\f'): ' ',
		ord('\r'): None
	}
	a = s.translate(remap)
	print a

	# remove all combining characters
	import unicodedata
	import sys
	cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
		if unicodedata.combining(chr(c)))
	b = unicodedata.normalize('NFD', a)
	print b
	print b.translate(cmb_chrs)

	# maps all Unicode decimal digit to ASCII
	digitmap = {c: ord('0')+unicodedata.digit(chr(c))
	for c in range(sys.maxunicode)
	if unicodedata.category(chr(c)) == 'Nd'}
	print len(digitmap)
	# Arabic digits
	x = '\u0661\u0662\u0663'
	print x.translate(digitmap)


def test_align_text():
	text = 'hello world'
	print text.ljust(20)
	print text.rjust(20)
	print text.center(20)

	# with fill character
	print text.center(20, '*')
	print format(text, '>20')
	print format(text, '^20')
	print format(text, '=^20s')
	print '{:>10s} {:>10s}'.format('hello', 'world')
	x = 1.2345
	print format(x, '>20')


def test_concatenation():

	def combine(source, maxsize):
		parts = []
		size = 0
		for part in source:
			parts.append(part)
			size += len(part)
			if size > maxsize:
				yield ''.join(parts)
				parts = []
				size = 0
		yield ''.join(parts)


def test_interpolating_variables_in_string():
	s = '{name} has {n} messages.'
	print s.format(name='Gao', n=20)

	# safesub when missing var
	class safesub(dict):
		def __missing__(self, key):
			return '{' + key + '}'
	import sys
	# Abandon: no format_map in 2.x
	def sub(text):
		return text.format_map(safesub(sys._getframe(1).f_locals))
	name = 'Gao'
	n = 20
	print sub('hello {name}')


def test_tokenize():
	Token = namedtuple('Token', ['type', 'value'])
	def generate_tokens(pat, text):
		scanner = pat.scanner(text)
		for m in iter(scanner.match, None):
			yield Token(m.lastgroup, m.group())

	NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
	NUM = r'(?P<NUM>\d+)'
	PLUS = r'(?P<PLUS>\+)'
	TIMES = r'(?P<TIMES>\*)'
	EQ = r'(?P<EQ>=)'
	WS = r'(?P<WS>\s+)'

	master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

	for tok in generate_tokens(master_pat, 'foo = 42'):
		print tok



def main():
	test_tokenize()




if __name__=='__main__':
	main()