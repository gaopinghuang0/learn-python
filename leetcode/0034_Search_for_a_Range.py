import unittest


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # idea: binary search
        if not nums:
            return [-1, -1]
        i, j = 0, len(nums)-1
        res = []
        while i <= j:
            mid = (i+j)//2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                ii, jj = i, mid
                while ii < jj:
                    mid = (ii+jj)//2
                    if nums[mid] < target:
                        ii = mid + 1
                    else:
                        jj = mid
                res.append(jj)
                ii, jj = mid, j
                while ii < jj:
                    mid = (ii+jj)//2 + 1
                    if nums[mid] > target:
                        jj = mid - 1
                    else:
                        ii = mid
                res.append(ii)
                break
        if not res:
            return [-1, -1]
        return res

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    self.assertEqual(self.s.searchRange([], 0), [-1, -1])
    self.assertEqual(self.s.searchRange([5], 0), [-1, -1])
    self.assertEqual(self.s.searchRange([5], 5), [0, 0])
    self.assertEqual(self.s.searchRange([5,5], 5), [0, 1])
    self.assertEqual(self.s.searchRange([5,5,7], 5), [0, 1])
    self.assertEqual(self.s.searchRange([5,5,5], 5), [0, 2])
    self.assertEqual(self.s.searchRange([5,7,7,8,8,10], 8), [3,4])


if __name__ == "__main__":
  unittest.main()
