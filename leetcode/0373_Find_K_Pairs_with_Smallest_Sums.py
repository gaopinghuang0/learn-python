import unittest

# idea from Submission, beats 36.27%
from heapq import heappush, heappop
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # idea2 from Discuss: do not compute all pairs
        # add all elements in nums1 with the first element in nums2,
        # then add more pair if necessary
        if k <= 0 or not nums1 or not nums2:
            return []
        hp = []
        n1 = len(nums1)
        n2 = len(nums2)
        n = min(n1, k)
        y = nums2[0]
        for i in range(n):
            heappush(hp, (nums1[i]+y, i, 0))
        res = []
        while hp and len(res) < k:
            _, i1, i2 = heappop(hp)
            res.append([nums1[i1], nums2[i2]])
            if i2 + 1 < n2:
                heappush(hp, (nums1[i1]+nums2[i2+1], i1, i2+1))
        return res


# very slow, beats 2.77%
from heapq import heappush, heappop
class SolutionSlow(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # idea 1: use min heap to store all possible combinations
        if not nums1 or not nums2:
            return []
        hp = []
        for num1 in nums1:
            for num2 in nums2:
                heappush(hp, (num1+num2, num1, num2))
        res = []
        for _ in range(k):
            _, num1, num2 = heappop(hp)
            res.append([num1, num2])
            if not hp:
                break
        return res




class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    print(self.s.kSmallestPairs(nums1, nums2, 3))


if __name__ == "__main__":
  unittest.main()
