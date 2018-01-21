

# slow, beats 0.51%
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = ''.join(S.split('-')).upper()
        size = len(s)
        i = size
        ans = []
        while i > K:
            ans.insert(0, s[i-K:i])
            i -= K
        ans.insert(0, s[:i])
        return '-'.join(ans).strip('-')
