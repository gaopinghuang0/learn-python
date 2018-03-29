import unittest

# beats 86.85%
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: sum of 0 to n minus total sum
        n = len(nums)
        total = n * (n+1) // 2
        return total - sum(nums)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # self.assertEqual(self.s.method(), None)
        pass


if __name__ == "__main__":
    unittest.main()
