import unittest

# beats 98.63%
class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # idea: recursion, sort first, start from the smallest x
        # filter a list of y so that y % x == 0, then recursively call on the list of y
        if len(nums) <= 1:
            return nums
        divisible = set()
        memo = {}  # {x: [y]}, x is not divisible by other nums in the list, while y % x == 0
        nums.sort()
        for i, x in enumerate(nums[:-1]):
            if x not in divisible:
                memo[x] = []
                for y in nums[i+1:]:
                    # since y can be divided by x, then y must be part of the larger set that contains x
                    # in other words, y cannot be a key in memo, so we skip it later
                    if y % x == 0:
                        memo[x].append(y)
                        divisible.add(y)
        ans = []
        # print(nums)
        # print(memo, divisible)
        for k, v in memo.items():
            rest = self.largestDivisibleSubset(v)
            if len(rest) + 1 > len(ans):
                ans = [k] + rest
        return ans

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.largestDivisibleSubset([1,2,3]), [1,2])
        self.assertEqual(self.s.largestDivisibleSubset([1,2,4,8]), [1,2,4,8])


if __name__ == "__main__":
    unittest.main()
