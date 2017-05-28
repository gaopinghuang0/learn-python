import unittest


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # start from two ends
        # if the sum is larger than target, decrease the right end
        # if the sum is smaller than target, increase the left end
        # return if matched
        left = 1
        right = len(numbers)
        while left < right:
          res = numbers[left-1] + numbers[right-1]
          if res > target:
            right -= 1
          elif res < target:
            left += 1
          else:
            return [left, right]
            
        return None



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # Note: numbers are already soted in ascending order
        self.assertEqual(self.s.twoSum([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(self.s.twoSum([2, 7], 9), [1, 2])
        self.assertEqual(self.s.twoSum([2, 3, 4], 6), [1, 3])
        self.assertEqual(self.s.twoSum([1, 3, 3, 4], 6), [2, 3])
        self.assertEqual(self.s.twoSum([-1, 3, 7], 6), [1, 3])
        # Cases below are not valid since there will be exactly one solution
        # self.assertEqual(self.s.twoSum([2, 2, 8, 7], 9), [1, 4])
        # self.assertEqual(self.s.twoSum([2, 3, 4, 2], 6), [1, 3])
        # self.assertEqual(self.s.twoSum([2, 3, 4, 3], 6), [1, 3])


if __name__ == "__main__":
    unittest.main()
