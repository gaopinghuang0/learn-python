import unittest


# beats 7.03%
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = -1
        res = 0
        for i, num in enumerate(nums):
            if num == 1:
                if i - prev > res:
                    res = i - prev
            else:
                prev = i
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.findMaxConsecutiveOnes([1,1,0,1,1,1]), 3)


if __name__ == "__main__":
    unittest.main()
