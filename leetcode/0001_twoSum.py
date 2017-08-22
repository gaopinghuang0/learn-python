class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # use dict to speed up
        d = {}
        for i, x in enumerate(nums):
        	if x in d:
        		return [d[x], i]
        	else:
        		d[target-x] = i

print Solution().twoSum([2, 7, 8, 9], 15)