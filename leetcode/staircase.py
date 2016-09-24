

def StairCase(n):
	s = ' '* n + '#' * n
	for i in xrange(1, n+1):
		print s[i:i+n]

StairCase(100)