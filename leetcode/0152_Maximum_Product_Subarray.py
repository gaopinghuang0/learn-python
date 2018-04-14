import unittest

# beats 98.41%
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea from Discuss, use two pointers to store the min and max up to x
        res = nums[0]
        _max, _min = res, res
        for val in nums[1:]:
            if val < 0:
                _max, _min = _min, _max

            _max = max(val, _max*val)
            _min = min(val, _min*val)
            if _max > res:
                res = _max
        return res


class SolutionWrong(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: when we meet 0, start over
        if not nums:
            return 0
        max_p = nums[0]
        prev_p = 1
        for num in nums:
            if num > max_p:
                max_p = num
            if num == 0:
                prev_p = 1
            else:
                prev_p *= num
                if prev_p > max_p:
                    max_p = prev_p
        return max_p


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        nums = [2,3,-2,4]
        self.assertEqual(self.s.maxProduct(nums), 6)
        nums = [0,0]
        self.assertEqual(self.s.maxProduct(nums), 0)
        nums = [1,0]
        self.assertEqual(self.s.maxProduct(nums), 1)
        nums = [2,3,-2,-4]
        self.assertEqual(self.s.maxProduct(nums), 48)
        nums = [-2]
        self.assertEqual(self.s.maxProduct(nums), -2)
        nums = [2,3,0,8,-2,0,-4]
        self.assertEqual(self.s.maxProduct(nums), 8)
        nums = [-2,0,-1]
        self.assertEqual(self.s.maxProduct(nums), 0)
        nums = [2,-5,-2,-4,3]
        self.assertEqual(self.s.maxProduct(nums), 24)

if __name__ == "__main__":
    unittest.main()
