import unittest

import itertools

class Solution(object):
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		return map(list, itertools.combinations(xrange(1, n+1), k))


class TestSolution(unittest.TestCase):
	def setUp(self):
		self.s = Solution()

	def test_method(self):
		"""Such as self.assertEqual, self.assertTrue"""
		print self.s.combine(4, 2)


if __name__ == "__main__":
	unittest.main()
