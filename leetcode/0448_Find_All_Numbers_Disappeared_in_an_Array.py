
# beats 7.79%, O(n) time and O(1) space
# although other methods are faster, they use O(n) space
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # idea: turn visited postive into negative, and stay negative if visit twice
        n = len(nums)
        for i in range(n):
            x = abs(nums[i]) - 1
            if x < n and nums[x] > 0:
                nums[x] *= -1
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res

obj = Solution()
print(obj.findDisappearedNumbers([4,3,2,7,8,2,3,1]))   # [5,6]

