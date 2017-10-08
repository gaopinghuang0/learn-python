
# Faster way: https://discuss.leetcode.com/topic/76205/python-dp/8
class Solution(object):
  def findTargetSumWays(self, nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    from collections import defaultdict
    memo = defaultdict(int)
    memo[0] = 1
    for n in nums:
      m = defaultdict(int)
      for i, v in memo.items():
        m[i+n] += v
        m[i-n] += v
      memo = m
    return memo[S]


# Correct but too slow
# class Solution(object):
#   def findTargetSumWays(self, nums, S):
#     """
#     :type nums: List[int]
#     :type S: int
#     :rtype: int
#     """
#     if not nums:
#       return 0
#     self.nums = nums
#     self.S = S
#     if not self.pre_check():
#       return 0
#     self.ans = 0
#     self.dfs(0, 0)
#     return self.ans

#   def pre_check(self):
#     total = sum(self.nums)
#     return -total <= self.S <= total

#   def dfs(self, pos, val):
#     if pos >= len(self.nums):
#       if val == self.S:
#         self.ans += 1
#       return
#     curr = self.nums[pos]
#     self.dfs(pos+1, val-curr)
#     self.dfs(pos+1, val+curr)

# [] 
# [1]
# [1,1]