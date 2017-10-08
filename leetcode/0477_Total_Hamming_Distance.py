
class Solution(object):
  def totalHammingDistance(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = map('{:032b}'.format, nums)
    ans = 0
    for b in zip(*nums):
      ans += b.count('0') * b.count('1')
    return ans
    

# too slow
# from itertools import combinations
# class Solution(object):
#   def totalHammingDistance(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if len(nums) < 2:
#       return 0
#     nums = map(lambda x: bin(x)[2:], nums)  
#     max_len = max(nums, key=len)
#     nums = map(lambda x: x.zfill(max_len), nums)
#     ans = 0
#     for a, b in combinations(nums, 2):
#       ans += self.hammingDistance(a,b)
#     return ans
  
#   def hammingDistance(self, a, b):
#     return sum([x==y for x,y in zip(a,b)])