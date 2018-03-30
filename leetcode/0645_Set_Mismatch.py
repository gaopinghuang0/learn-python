
# O(n) time and O(1) space 
# idea from Discuss, beats 56.03%
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # idea: O(n) time and O(1) space 
        # for current element value, set nums[value-1] as negative to indicate
        # that it occurs once
        # also, to find the missing one, use the sum of 1 to n and the real sum
        n = len(nums)
        total = n * (n+1) // 2
        real_sum = 0
        res = [0, 0]
        for i, val in enumerate(nums):
            val = abs(val)
            real_sum += val
            if nums[val-1] < 0:
                res[0] = val
            else:
                nums[val-1] = -nums[val-1]
        # use math relation of both sum
        res[1] = total - real_sum + res[0]
        return res

