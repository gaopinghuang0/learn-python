import unittest

# optimize based on other's submission
# beats 99.91%
from collections import defaultdict
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = defaultdict(int)
        for num in nums:
                count[num] += 1

        res = []
        if 0 in count and count[0] > 2:
            res.append([0,0,0])

        keys = count.keys()
        pos = sorted([k for k in keys if k > 0])
        neg = sorted([k for k in keys if k < 0])

        for p in pos:
            for n in neg:
                other = -(p+n)
                if other in count:
                    if other == p and count[p] > 1:
                        res.append([n,p,p])
                    elif other == n and count[n] > 1:
                        res.append([n,n,p])
                    elif n < other < p:
                        res.append([n, other, p])
        return res

class Solution_V1(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        size = len(nums)
        for i in xrange(size-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, size-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res


# time limit exceeded
# class Solution(object):
#   def threeSum(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     """
#     # idea: from left to right, keep nums[i], find all pairs of elements from nums[i+1:]
#     # that add up to -nums[i]
#     # one important fact: the set of unique triplets must be unique
#     # otherwise, suppose that 
#     # 1) two unique triplets have the same set {a,b,c}, contradict since they are duplicate
#     # 2) two unique triplets have the same set {a,b}, then 2a+b=0 and a+2b=0 ==> a==b, 
#     # contradict because the set is {a} not {a,b}
#     # 3) two unique triplets have the same set {a}, contradict since they are duplicate
#     res = {}  # {set(triplet): triplet}
#     for i, num in enumerate(nums):
#       for pair in self.twoSum(nums[i+1:], -num):
#         triplet = [num] + pair
#         if frozenset(triplet) not in res:
#           res[frozenset(triplet)] = triplet
#     return res.values()

#   def twoSum(self, arr, target):
#     d = {}
#     for i, x in enumerate(arr):
#       if x in d:
#         yield [target-x, x]
#       else:
#         d[target-x] = True



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        nums = [-1, 0, 1, 2, -1, -4]
        print self.s.threeSum(nums)
        print [[-1, 0, 1],  [-1, -1, 2]]

        nums = [-1, 2, -1, -1, -4]
        print self.s.threeSum(nums)
        print [[-1, 2, -1]]


        nums = [-1, 2, -1, 2, -4]
        print self.s.threeSum(nums)
        print [[-1, 2, -1], [2, 2, -4]]


if __name__ == "__main__":
    unittest.main()
