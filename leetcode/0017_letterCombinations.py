class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
        	6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        res = []
        for digit in digits:
        	if not res:
        		res = list(d[int(digit)])
        	else:
        		res = [s+c for s in res for c in d[int(digit)]]
        return res

print Solution().letterCombinations('234')