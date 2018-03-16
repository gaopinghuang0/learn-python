import unittest


# idea from Discuss, beats 71.25%
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # idea from Discuss, similar to 315 count smaller numbers after self
        # merge sort, count[i] =   lower <= s[j] - s[i] <= upper, when j > i
        # return sum(count)
        if not nums:
            return 0

        # first compute prefix sum
        # the first element must be 0
        pre_sum = [0]
        for n in nums:
            pre_sum.append(pre_sum[-1] + n)
        # print(pre_sum)
        
        def sort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            count = sort(lo, mid) + sort(mid, hi)

            # two pointers to compute count
            # O(n) since two pointers only increase and never decrease
            j = k = mid
            for left in pre_sum[lo:mid]:
                while j < hi and pre_sum[j] - left < lower:
                    j += 1
                while k < hi and pre_sum[k] - left <= upper:
                    k += 1
                count += (k - j)

            # do sort
            pre_sum[lo:hi] = sorted(pre_sum[lo:hi])
            # print(lo, hi, pre_sum[lo:hi], count)
            return count

        return sort(0, len(pre_sum))


from collections import defaultdict
class SolutionWrong(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # idea2: use a cache to store all possible sum
        cache = defaultdict(int)
        for x in nums:
            temp = cache.copy()
            for _sum in cache:
                temp[_sum+x] += 1
            temp[x] += 1
            cache = temp
        print(cache)
        return sum([count for _sum, count in cache.items() if lower <= _sum <= upper])


# Wrong idea
class SolutionWrong(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # idea: divide and conquer
        # divide into two halves, then consider the middle two elements
        if not nums:
            return 0

        def divide(nums, left, right, lower, upper):
            if left > right:
                return 0
            if left == right:
                return int(lower <= nums[left] <= upper)
            middle = (left+right) // 2
            res = 0
            res += divide(nums, left, middle, lower, upper)
            res += divide(nums, middle+1, right, lower, upper)
            # start to count num involving the middle two elements
            val = nums[middle] + nums[middle+1]
            res += lower <= val <= upper
            for i in range(1, right-middle):
                val1 = val + nums[middle+1+i]
                res += lower <= val1 <= upper
                val2 = val + nums[middle-i]
                res += lower <= val2 <= upper
                val = val1 + nums[middle-i]
                res += lower <= val <= upper
            if (right - left) % 2 == 0:  # odd nums, add the left most element
                val += nums[left]
                res += lower <= val <= upper
            return res

        return divide(nums, 0, len(nums)-1, lower, upper)


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    nums = [-2, 5, -1]
    # self.assertEqual(self.s.countRangeSum(nums, -2, 2), 3)
    nums = [-2,5,-1, 3, 5, -4]
    self.assertEqual(self.s.countRangeSum(nums, -2, 2), 5)
    nums = [-3,1,2,-2,2,-1]
    # self.assertEqual(self.s.countRangeSum(nums, -3, -1), 3)

if __name__ == "__main__":
  unittest.main()
