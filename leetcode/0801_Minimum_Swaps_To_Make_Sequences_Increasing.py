
# idea from Discuss, beats 99.40%
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # idea from Discuss, finite state
        # credit: https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss/119835/Java-O(n)-DP-Solution
        # swap means for the ith element in A and B, the min swaps if we swap A[i] and B[i]
        # hold means the min swaps if we DO NOT swap A[i] and B[i]
        swap, hold = 1, 0
        for i in range(1, len(A)):
            if A[i-1] >= B[i] or B[i-1] >= A[i]:
                # the ith manipulation should be the same as i-1th, namely,
                # if we swap at i-1, we must swap at i, otherwise, it's not strictly increasing
                # hold = hold
                swap += 1
            elif A[i-1] >= A[i] or B[i-1] >= B[i]:
                # the ith manipulation should be the opposite of i-1th, namely,
                # if we swap at i-1, we must hold at i
                swap, hold = hold+1, swap
            else:
                # either swap or hold is OK, let's keep the min one
                _min = min(swap, hold)
                swap, hold = _min+1, _min
        return min(swap, hold)


class Solution_Wrong(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # idea: count the number of inversion pair
        a_inv = set()
        b_inv = set()
        prev_a, prev_b = A[0], B[0]
        for i in range(1, len(A)):
            if A[i] <= prev_a:
                a_inv.add(i)
            if B[i] <= prev_b:
                b_inv.add(i)
            prev_a = A[i]
            prev_b = B[i]

        return len(a_inv.union(b_inv))

sol = Solution()
A = [1,3,5,4]
B = [1,2,3,7]
print(sol.minSwap(A, B)) # 1
A = [1,7,4,5]
B = [0,3,8,9]
print(sol.minSwap(A, B)) # 1
A = [0,4,4,5,9]
B = [0,1,6,8,10]
print(sol.minSwap(A, B)) # 1
A = [3,3,8,9,10]
B = [1,7,4,6,8]
print(sol.minSwap(A, B)) # 1
