
# beats 98.98%
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: DP, similar to 0309_Best_Time_to_Buy_and_Sell_Stock_with_Cooldown
        # use a dict to store the count, and sort the keys[m]
        # use pick[i] and hold[i] to store the max earn if we pick or hold keys[i]
        # Two cases:
        # 1. if keys[i] > keys[i-1]+1, meaning we can pick freely
        # then pick[i] = max(pick[i-1], hold[i-1]) + point
        # 2. if keys[i] == keys[i-1]+1, meaning we can only pick keys[i] if we held keys[i-1]
        # pick[i] = hold[i-1]+point
        # in both cases, hold[i] = max(pick[i-1], hold[i-1]) since we can always get the 
        # larger one if we choose to hold keys[i]
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1
        sorted_keys = sorted(cnt.keys())
        pick, hold = 0, 0  # max earn if we decide to pick or hold
        last = -1
        for num in sorted_keys:
            point = cnt[num]*num
            if num != last + 1:  # can pick freely
                pick, hold = max(pick, hold)+point, max(pick, hold)
            else:
                pick, hold = hold+point, max(pick, hold)
            last = num
        return max(pick, hold)

sol = Solution()
nums = [3,4,2]
print(sol.deleteAndEarn(nums))  # 6
nums = [2,2,3,4,3,3]
print(sol.deleteAndEarn(nums))  # 9
nums = [2,4,6,2]
print(sol.deleteAndEarn(nums))  # 14
nums = [2,2,3,3,3,4,4,8,9]
print(sol.deleteAndEarn(nums))  # 21
nums = [10,8,4,2,1,3,4,8,2,9,10,4,8,5,9,1,5,1,6,8,1,1,6,7,8,9,1,7,6,8,4,5,4,1,5,9,8,6,10,6,4,3,8,4,10,8,8,10,6,4,4,4,9,6,9,10,7,1,5,3,4,4,8,1,1,2,1,4,1,1,4,9,4,7,1,5,1,10,3,5,10,3,10,2,1,10,4,1,1,4,1,2,10,9,7,10,1,2,7,5]
print(sol.deleteAndEarn(nums))  # 338

