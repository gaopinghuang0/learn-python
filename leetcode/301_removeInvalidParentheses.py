# 301_removeInvalidParentheses.py

# Credit: https://discuss.leetcode.com/topic/28833/short-python-bfs
# Author: StefanPochmann
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(s):
            s = filter('()'.count, s)   # keep all '()' chars
            while '()' in s:
                s = s.replace('()', '')
            return not s
        level = {s}
        while True:
            valid = filter(is_valid, level)
            if valid:
                return valid
            level = {s[:i]+s[i+1:] for s in level for i in range(len(s))}



s = "()())()"
print Solution().removeInvalidParentheses(s)