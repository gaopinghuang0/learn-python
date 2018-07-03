import unittest

# beats 7.18%
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: sort the array and sum up 0-th, 2-th, ..., (2n-1)-th num
        return sum(sorted(nums)[::2])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.arrayPairSum([1,4,3,2]), 4)
        self.assertEqual(self.s.arrayPairSum([-8,1,4,3,2,-6,2,4]), -1)


if __name__ == "__main__":
    unittest.main()
