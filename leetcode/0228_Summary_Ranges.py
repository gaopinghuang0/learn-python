
# beats 27.05%
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return nums
        res = []
        start = end = nums[0]
        for num in nums[1:]:
            if num == end + 1:  # consecutive
                end = num
            else:
                self.add_summary(res, start, end)
                start = end = num
        self.add_summary(res, start, end)
        return res

    def add_summary(self, res, start, end):
        if start == end:
            res.append(str(start))
        else:
            res.append('{}->{}'.format(start, end))


sol = Solution()
nums = [0,1,2,4,5,7]
print(sol.summaryRanges(nums))
nums = [-1, 0,2,3,4,6,8,9]
print(sol.summaryRanges(nums))
