
import itertools
import math
# idea from Discuss, beats 36.99%
# https://leetcode.com/problems/24-game/discuss/107675/short-python
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # idea from Discuss
        if len(nums) == 1:
            return math.isclose(nums[0], 24)
        return any(self.judgePoint24([x]+rest)
                   for a, b, *rest in itertools.permutations(nums)
                   for x in {a+b, a-b, a*b, b and a/b})
                   # use a set to dedup, b and a/b to prevent divide by 0

sol = Solution()
print(sol.judgePoint24([4,1,8,7]))  # True
print(sol.judgePoint24([1,3,4,6]))  # True
print(sol.judgePoint24([1,2,1,2]))  # False