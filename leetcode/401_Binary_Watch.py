import unittest

# Credit: https://discuss.leetcode.com/topic/59374/simple-python-java
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for i in xrange(0, 12):
        	for j in xrange(0, 60):
        		if (bin(i) + bin(j)).count('1') == num:
        			res.append('%d:%02d'%(i,j))
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        print self.s.readBinaryWatch(1)


if __name__ == "__main__":
    unittest.main()
