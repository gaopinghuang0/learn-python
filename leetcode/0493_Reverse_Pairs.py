# beats 77.53%
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: merge sort
        # two pointers on left and right halves
        # j > i and nums[i] > 2*nums[j]
        if not nums:
            return 0

        def sort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            count = sort(lo, mid) + sort(mid, hi)
            j = mid
            for i in range(lo, mid):
                while j < hi and nums[i] > 2 * nums[j]:
                    j += 1
                    count += (mid - i)  # since all elements from i to mid will be larger than 2*nums[j]
            nums[lo:hi] = sorted(nums[lo:hi])
            return count

        return sort(0, len(nums))

obj = Solution()
print(obj.reversePairs([1,3,2,3,1]))  # 2
print(obj.reversePairs([2,4,3,5,1]))  # 3
print(obj.reversePairs([5,4,3,2,1]))  # 4
