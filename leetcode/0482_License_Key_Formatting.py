
# beats 60.46%
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.replace('-', '').upper()
        size = len(s)
        if size < K:
            return s
        i = K if size % K == 0 else size % K
        ans = [s[:i]]
        while i < size:
            ans.append(s[i:i+K])
            i += K
        return '-'.join(ans)


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
