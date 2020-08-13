
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # idea: divide and conquer.
        # From Discuss: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/discuss/780880/DP-with-picture-(Burst-Balloons)
        # Similar problems:
        # 312. Burst Balloons
        # 1000. Minimum Cost to Merge Stones
        # 1039. Minimum Score Triangulation of Polygon
        
        cuts.append(0)
        cuts.append(n)
        cuts.sort()

        m = len(cuts)
        dp = [[None] * (m+1) for _ in range(m+1)]
        # i, j are non-inclusive boundary
        def helper(i, j, cuts):
            if j - i <= 1:
                return 0
            
            if dp[i][j] is not None:
                return dp[i][j]
            
            dp[i][j] = min(cuts[j] - cuts[i] + helper(i, k, cuts) + helper(k, j, cuts)
                for k in range(i+1, j))
            return dp[i][j]
        
        return helper(0, len(cuts) - 1, cuts)


# Greedy algorithm, wrong.
class Solution_Wrong:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # idea: find the value closest to the mid value, then divide and conquer
        
        def helper(lo, hi, cuts):
            if len(cuts) == 0:
                return 0
            if len(cuts) == 1:
                return hi - lo
            
            cuts.sort()
            mid = (lo + hi) // 2
            left = bisect.bisect_left(cuts, mid)
            if left == len(cuts):  # is rightmost
                return hi - lo + helper(lo, cuts[left-1], cuts[:left-1])
            if cuts[left] == mid or left == 0:  # is mid or leftmost
                return hi - lo + helper(lo, cuts[left], cuts[:left]) + helper(cuts[left], hi, cuts[left+1:])
            
            diff1 = mid - cuts[left-1]
            diff2 = cuts[left] - mid
            if diff1 < diff2:  # left-1 is closer to mid
                return hi - lo + helper(lo, cuts[left-1], cuts[:left-1]) + helper(cuts[left-1], hi, cuts[left:])
            elif diff1 > diff2:
                return hi - lo + helper(lo, cuts[left], cuts[:left]) + helper(cuts[left], hi, cuts[left+1:])
            else:  # diff1 == diff2
                    # compare both scenario
                    return hi - lo + min(helper(lo, cuts[left-1], cuts[:left-1]) + helper(cuts[left-1], hi, cuts[left:]),
                                        helper(lo, cuts[left], cuts[:left]) + helper(cuts[left], hi, cuts[left+1:]))
            
        
        return helper(0, n, cuts)