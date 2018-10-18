import unittest

# idea from Submission
class Solution(object):
    def minWindow(self, s, t):
        need = collections.defaultdict(int)
        for ch in t: 
            need[ch] += 1
        missing = len(t)                         
        start, end = 0, 0
        i = 0
        for j, char in enumerate(s, 1): 
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:      
                while i < j and need[s[i]] < 0:  
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1                   
                missing += 1                     
                if end == 0 or j-i < end-start:  
                    start, end = i, j
                i += 1                           
        return s[start:end]

# Modifed from template:
# https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems
from collections import defaultdict
class Solution(object):
  def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    # note: t may have duplicate chars, all of them need to match within s 
    char_map = defaultdict(int)
    counter, begin, end = 0, 0, 0
    d = len(s) + 1
    head = 0
    for c in t:
      char_map[c] += 1
    while end < len(s):
      if char_map[s[end]] > 0:
        counter += 1
      char_map[s[end]] -= 1   # decrease 1 for any char, might be negative for irrelevant char
      end += 1
      while counter >= len(t):  # valid
        if end - begin < d:
          d = end - begin
          head = begin
        char_map[s[begin]] += 1   # increase 1 for any char
        if char_map[s[begin]] > 0:  # make it invalid if char exists in t
          counter -= 1
        begin += 1
    return '' if d == len(s) + 1 else s[head:head+d]
    


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.minWindow("ADOBECODEBANC", "ABC"), "BANC")
    self.assertEqual(self.s.minWindow("a", "aa"), "")
    self.assertEqual(self.s.minWindow("aa", "aa"), "aa")
    self.assertEqual(self.s.minWindow("ab", "abc"), "")
    self.assertEqual(self.s.minWindow("ab", "c"), "")


if __name__ == "__main__":
  unittest.main()
