import collections

class Solution(object):
    def __init__(self):
        self.cache = collections.defaultdict(list)

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        n = len(s)
        size = n
        while size > 0:
            if self.is_palindrome(s[:size]):
                if size == n:
                    res.append([s])
                else:
                    right = s[size:]
                    if right in self.cache:
                        right_res = self.cache[right]
                    else:
                        right_res = self.partition(right)
                    for r in right_res:
                        if size + len("".join(r)) == n:
                            res.append([s[:size]]+r)
            size -= 1
        self.cache[s] = res
        return res
                
    def is_palindrome(self, s):
        return s == s[::-1]


s = 'abcaa'
# [aavaa] [a ava a]  [aa v aa] [a a v a a]
# 'abcaa' => [a b c aa] [a b c a a]
sol = Solution()
print sol.partition(s)