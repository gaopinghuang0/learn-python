import unittest


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if not nums:
            dp = []
        else:
            n = len(nums)
            dp = [nums[0]]
            for i in xrange(1, n):
                dp.append(dp[i-1] + nums[i])
        self.dp = dp
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.dp:
            return 0
        if j >= len(self.dp):
            return self.dp[-1]
        if i <= 0:
            return self.dp[j]
        return self.dp[j] - self.dp[i-1]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = NumArray([-1, 2, 3, 4, -6])

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.sumRange(2, 3), 7)


if __name__ == "__main__":
    unittest.main()
