
# optimize, done in O(n) but stop if find two equal remainders
class Solution(object):
  def checkSubarraySum(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    n = len(nums)
    if n < 2:
      return False
    if k == 0:
      for i in range(n-1):
        if nums[i:i+2] == [0,0]:
          return True
      return False
    if n >= abs(k)+1:  # because there are at most k diff remainder, at least two will be the same
      return True

    d = {0: -1}
    total = 0
    for i, x in enumerate(nums):
      total += x
      m = total % k
      if m not in d:
        d[m] = i
      elif d[m] + 1 < i:  # at least len 2
        return True
    return False


# done in O(n)
# from collections import Counter
# class Solution(object):
#   def checkSubarraySum(self, nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: bool
#     """
#     # idea: use 1D dp, dp[i] is the sum of nums[:i]
#     # get the remainder after mod k
#     # if at least two values i,j have the same remainder True
#     # because dp[j] - dp[i] == 0 mod k
#     n = len(nums)
#     if n < 2:
#       return False
#     if k == 0:
#       for i in range(n-1):
#         if nums[i:i+2] == [0,0]:
#           return True
#       return False
#     if n >= abs(k)+1:  # because there are at most k diff remainder, at least two will be the same
#       return True
#     dp = [nums[0] % k]
#     for x in nums[1:]:
#       dp.append((dp[-1]+x) % k)
#     count = Counter(dp)
#     if count.most_common(1)[0][1] >= 2:
#       return True
#     elif count[0] == 1 and dp[0] != 0:
#       return True
#     else:
#       return False
