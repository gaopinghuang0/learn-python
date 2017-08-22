class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        size = n
        res = []
        while size > 0:
            if self.is_palindrome(s[:size]):
                if size == n:
                    return 0
                else:
                    res.append(1 + self.minCut(s[size:]))
            size -= 1
        return min(res)

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
                    for r in self.partition(s[size:]):
                        if size + len("".join(r)) == n:
                            res.append([s[:size]]+r)
            size -= 1
        return res
                
    def is_palindrome(self, s):
        return s == s[::-1]


s = 'aab'
# 'aab' => 1
# aavaa => 0 [a ava a]  [aa v aa] [a a v a a]
# 'abcaa' => [a b c aa] [a b c a a]
sol = Solution()
print sol.minCut(s)