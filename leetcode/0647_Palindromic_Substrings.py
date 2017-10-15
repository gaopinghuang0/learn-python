class Solution(object):
  def countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    count = 0
    n = len(s)
    for i in range(n):
      j = 0
      while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
        j += 1
        count += 1
      j = 0
      while i-j >= 0 and i+j+1 < n and s[i-j] == s[i+j+1]:
        j += 1
        count += 1
    return count