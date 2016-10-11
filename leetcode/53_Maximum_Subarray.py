import unittest


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Every time to calculate the max sum starting from 0 end with n, 
        # we either take sum(nums[0:n-1])+nums[n] or nums[n], whichever is larger. 
        # In other words, if sum(nums[0:n-1)] is less than 0, 
        # than we will drop the nums[0:n-1].
        ret = -9999
        prevsum = nums[0]

        for i in range(1, len(nums)):
            prevsum = max(nums[i], nums[i]+prevsum)
            ret = max(ret, prevsum)
        return max(nums[0], ret)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        d = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(self.s.maxSubArray(d), 6)
        d = [-2, -1]
        self.assertEqual(self.s.maxSubArray(d), -1)
        d = [1, 2]
        self.assertEqual(self.s.maxSubArray(d), 3)



if __name__ == "__main__":
    unittest.main()
