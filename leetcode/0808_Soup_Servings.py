
import math

# idea from Discuss: recursion with memo, beats 56.99%
class Solution(object):
    memo = {} # global memo shared by more test cases
    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        # idea from Discuss: recursion with memo
        # credit: https://leetcode.com/problems/soup-servings/discuss/121711/C++JavaPython-When-N-greater-4800-just-return-1
        # key idea is that we treat 25ml as a unit, i.e., 1 serving = 25 ml
        # then 100ml means 4 serving
        # we do not use f(a-100, b) because the space complexity will be much larger
        if N > 4800: return 1  # because the chance is very close to 1
        def f(a, b):
            if (a, b) in self.memo: return self.memo[a, b]
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1
            if b <= 0: return 0
            self.memo[(a,b)] = 0.25 * (f(a-4, b) + f(a-3, b-1) + f(a-2, b-2) + f(a-1, b-3))
            return self.memo[(a,b)]
        N = math.ceil(N / 25.0)
        return f(N, N)

sol = Solution()
print(sol.soupServings(50))  # 0.625