class Solution(object):                                                                                                              
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        # if n == 0:
        #     return 0
        while n != 0:
            n, m = divmod(n, 2)
            res += m
        return res

obj = Solution()
for n in [2, 11]:
    print obj.hammingWeight(n)
