

# beats 56.41%
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        m = set(J)
        res = 0
        for s in S:
            if s in m:
                res += 1
        return res
