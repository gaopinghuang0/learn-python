
# idea from other's submission, beats 98.14%
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # idea from other's submission
        # for each length, check if all subarrays with this length in A
        # exist in B
        def check(length):
            seen = set(tuple(A[i:i+length]) for i in range(len(A)-length+1))
            return any(tuple(B[j:j+length]) in seen for j in range(len(B)-length+1))

        lo, hi = 0, min(len(A), len(B)) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1


# still slow
# idea from Discuss, 2D dp, beats 6.33%
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # idea from Discuss, 2D dp
        # dp[i][j] is the length of longest common subarray ending with A[i] and B[j]
        if not A or not B:
            return 0
        m, n = len(A), len(B)
        res = 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    res = max(res, dp[i][j])
        return res




# Time Limit Exceeded
from collections import defaultdict
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # idea: use a dict to store the index of B
        if not A or not B:
            return 0

        b_lookup = defaultdict(list)
        for i,v in enumerate(B):
            b_lookup[v].append(i)
        # print(b_lookup)

        # two pointers for subarray of A
        i, j = 0, 0
        n = len(A)
        res = 0
        while j < n:
            if A[j] in b_lookup:
                next_move_idx = b_lookup[A[j]]
                while next_move_idx:
                    res = max(res, j-i+1)
                    temp = []
                    j += 1
                    if j >= n:
                        break
                    for idx in next_move_idx:
                        next_idx = idx+1
                        if next_idx < n and B[next_idx] == A[j]:
                            temp.append(next_idx)
                    next_move_idx = temp
                i += 1
                j = i
            else:
                j += 1
                i = j
        return res

obj = Solution()
A = [1,2,3,2,1]
B = [3,2,1,4,7]
print(obj.findLength(A, B))
A = [1,4,8,2,3,2,1,5,6,7]
B = [3,2,1,4,7,2,1,5,6,7]
print(obj.findLength(A, B))
