class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s = ''
        res = []
        self.cur(res, n, n, s)
        return res
    
    def cur(self, res, left, right, s):
        # first assume s is prev string
        # whenever the left count is greater than 0, we just add a open parenthesis
        # whenever the right count is greater than the left, we add a close parenthesis
        if left == 0 and right == 0:
            res.append(s)
        if left > 0:
            self.cur(res, left-1, right, s+'(')
        if left < right:
            self.cur(res, left, right-1, s+')')
        
n = 5
print Solution().generateParenthesis(n)