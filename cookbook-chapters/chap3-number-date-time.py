#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate
from decimal import Decimal, localcontext
import numpy as np
from datetime import datetime
from pytz import timezone, country_timezones

def test_rounding():
	print round(1.5)
	print round(2.5)
	print round(1.5) == round(2.5) 
	a = 1627731
	print round(a, -1)
	print round(a, -2)


def test_decimal():
	a = Decimal('4.2')
	b = Decimal('2.1')
	print a+b  # not 6.3000000000001
	print a+b == Decimal('6.3')
	a = Decimal('1.3')
	b = Decimal('1.7')
	print a/b
	with localcontext() as ctx:
		ctx.prec = 3
		print a/b


def test_format():
	x = 1234.56789
	print format(x, '0.2f')
	print format(x, '>10.1f')
	# Inclusion of thousands separator
	print format(x, ',')
	print format(x, '0,.1f')

def test_numpy():
	m = np.matrix([[1, -2, 3], [0, 4, 5], [7,8,-9]])
	print m
	print 'transpose'
	print m.T
	print 'inverse'
	print m.I  
	v = np.matrix([[2], [3], [4]])
	print m*v
	import numpy.linalg
	print numpy.linalg.det(m)
	print numpy.linalg.eigvals(m)
	print 'solve for x in mx = v'
	x = numpy.linalg.solve(m, v)
	print x

def test_time_zone():
	d = datetime(2016, 01, 16, 23, 18)
	print d
	print 'localize the date for Chicago'
	central = timezone('US/Central')
	loc_d = central.localize(d)
	print loc_d
	print 'convert to Chongqing time'
	cq_d = loc_d.astimezone(timezone('Asia/Chongqing'))
	print cq_d
	print 'consider the one-hour daylight saving time'
	cq_d2 = timezone('Asia/Chongqing').normalize(cq_d)
	print cq_d2
	print 'consult timezone list of China'
	print country_timezones('CN')


def main():
	test_time_zone()




if __name__=='__main__':
	main()