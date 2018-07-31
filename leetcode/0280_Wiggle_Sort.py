import unittest


# optimize, idea from Submission, beats 100%
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1, n, 2):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
            if i+1 < n and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

# beats 6.92%
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        up = True
        n = len(nums)
        for i in range(1, n):
            if up and nums[i-1] > nums[i]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            elif not up and nums[i-1] < nums[i]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            up = not up



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
    unittest.main()
