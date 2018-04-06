import unittest

# optimize based on other Submission
# beats 73.09%
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: two pointers and a counter
        i = 0
        for x in nums:
            if i < 2 or x > nums[i-2]:
                nums[i] = x
                i += 1
        return i

# beats 27.29%
class SolutionSlow(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: two pointers and a counter
        if len(nums) < 3:
            return len(nums)

        i = 0
        count = 0
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                if count == 0:
                    count += 1  # allowed
                    i += 1
                    nums[i] = nums[j]
            else:
                i += 1
                nums[i] = nums[j]
                count = 0
        return i+1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        nums = [1,1,1]
        self.assertEqual(self.s.removeDuplicates(nums), 2)
        print(nums)
        nums = [-1,0,1,1,1,2,2,2,2,3]
        self.assertEqual(self.s.removeDuplicates(nums), 7)
        print(nums)
        self.assertEqual(nums[:7], [-1, 0, 1, 1, 2, 2, 3])
        nums = [1,1,1,1,3,3]
        self.s.removeDuplicates(nums)
        print(nums)

if __name__ == "__main__":
    unittest.main()
