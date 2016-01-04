#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate
from collections import Counter

def test_counter():
	words = [
       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under'
	]
	word_counts = Counter(words)
	# print word_counts
	# print word_counts['eyes']
	top_three = word_counts.most_common(3)
	# print top_three
	morewords = ['why','are','you','not','looking','in','my','eyes']
	word_counts.update(morewords)
	# print word_counts
	a = Counter(words)
	b = Counter(morewords)
	# Combine counts
	c = a + b
	# Substract counts
	d = a - b
	print c
	print d





def main():
	test_counter()


if __name__=='__main__':
	main()
