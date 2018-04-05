import unittest


# idea from Discuss O(n) timea and O(1) space
# beats 55.38%
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea from Discuss O(n) timea and O(1) space
        # put each number in its right place
        # for example, if we find 5, swap with nums[4]
        n = len(nums)
        for i in range(n):
            # while is the key, keep swapping
            # each element will be visited at most twice
            while nums[i] > 0 and nums[i] <= n and nums[nums[i]-1] != nums[i]:
                a, b = nums[nums[i]-1], nums[i]
                nums[i], nums[b-1] = a, b

        # find the first place where the number is not right
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.firstMissingPositive([1,2,0]), 3)
        self.assertEqual(self.s.firstMissingPositive([3,4,-1,1]), 2)


if __name__ == "__main__":
    unittest.main()
