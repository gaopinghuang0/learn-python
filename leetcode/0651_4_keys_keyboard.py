"""
Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.
Key 2: (Ctrl-A): Select the whole screen.
Key 3: (Ctrl-C): Copy selection to buffer.
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.
"""

class Solution:
    def maxA(self, N: int) -> int:
        # idea: the last key press is either A or Ctrl-V.
        dp = list(range(1, N+1))  # press A
        for i in range(1, N):
            # if press Ctrl-V at i, assume we consecutively press Ctrl-V from j to i,
            # which implies j-2 is Ctrl-A, j-1 is Ctrl-C.  Note that j could be anywhere
            # between 2 and i.
            for j in range(2, i):
                dp[i] = max(dp[i], dp[j-2] * (i-j+1))
        return dp[N-1]

sol = Solution()
print(sol.maxA(3))  # 3
print(sol.maxA(7))  # 9

for i in range(1, 21):
    print(i, sol.maxA(i))