import unittest

# optimize by other's submission, beats 93.39%
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(nums, target, N, path, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers for sorted 2-sum
                l, r = 0, len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(path+[nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or nums[i-1] != nums[i]:
                        findNsum(nums[i+1:], target-nums[i], N-1, path+[nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results


# beats 48.03%
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for three in self.threeSum(nums[i+1:], target-nums[i]):
                res.append([nums[i]] + three)
        return res

    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # copied from 15_3Sum
        res = []
        size = len(nums)
        for i in range(size-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, size-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
