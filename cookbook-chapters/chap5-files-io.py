#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from functools import partial
import gzip, bz2
import os
import time

RECORD_SIZE = 32

def test_print():
	row = ('Acme', 50, 991.5)
	print(*row, sep=', ')


def write_to_existing_file():
	with open('somefile', 'wt') as f:
		print('Hello\n', file=f)
	with open('somefile', 'xt') as f:
		print('Hello\n', file=f)

def compressed_file_io():
	with gzip.open('somefile.gz', 'rt') as f:
		text = f.read()

	# or
	with bz2.open('somefile.bz2', 'rt') as f:
		text = f.read()

def iterate_fix_sized_records():
	with open('somefile.data', 'rb') as f:
		records = iter(partial(f.read, RECORD_SIZE), b'')
		for r in records:
			pass

def file_metadata():
	# to some extent, this can show whether the laptop was old or new
	path = '/etc/passwd'
	print(os.path.getsize(path))
	print(os.path.getmtime(path))
	print(time.ctime(os.path.getmtime(path)))


def main():
	file_metadata()




if __name__=='__main__':
	main()