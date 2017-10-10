
# shorter
class Solution(object):
  def validPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    n = len(s) 
    if n <= 2:
      return True
    for i in xrange(n):
      if s[i] != s[n-i-1]:
        x = s[i:n-i-1]
        y = s[i+1:n-i]
        return x == x[::-1] or y == y[::-1]
    return True

# Correct and fast
# class Solution(object):
#   def validPalindrome(self, s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     n = len(s) 
#     if n <= 2:
#       return True
#     i,j = 0, n-1
#     while i < j:
#       if s[i] == s[j]:
#         i += 1
#         j -= 1
#       else:
#         x = s[i:j]
#         y = s[i+1:j+1]
#         return x == x[::-1] or y == y[::-1]
#     return True