#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate
from collections import Counter


def main():
	cnt = Counter()
	for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
		cnt[word] += 1
	print cnt

if __name__=='__main__':
	main()
