import unittest

# beats 71.76%
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # idea: binary search
        if not nums:
            return False

        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) / 2
            cur = nums[mid]
            if cur == target:
                return True

            if cur > nums[low]:  # left side is sorted
                if target >= nums[low] and cur >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            elif cur < nums[low]:  # right side is sorted
                if target >= cur and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:  # duplicate
                low += 1
        return nums[high] == target




if __name__ == "__main__":
    unittest.main()
