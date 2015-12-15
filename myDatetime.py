#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals # boilerplate
from datetime import timedelta

def test_timedelta():
	year = timedelta(days=365)
	# add up to 365 days
	another_year = timedelta(weeks=40, days=84, hours=23, 
							minutes=50, seconds=600)
	print year.total_seconds()
	print year == another_year
	ten_years = 10 * year
	print ten_years, ten_years.days // 365
	nine_years = ten_years - year
	print nine_years, nine_years.days // 365
	three_years = nine_years // 3
	print three_years, three_years.days // 365
	print abs(three_years - ten_years) == 2 * three_years + year



def main():
	test_timedelta()

if __name__=='__main__':
	main()