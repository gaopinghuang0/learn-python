import unittest

# idea from Discuss, beats 79.49%
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        # idea from Discuss
        def prep(nums, k):
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a+b]

        return max(merge(prep(nums1, i), prep(nums2, k-i))
                   for i in range(k+1)
                   if i <= len(nums1) and k-i <= len(nums2))

class Solution_Slow(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        # idea: recursion
        # pick one digit, if the number of the remaining digits is greater than or equal to k-1
        # then we can consider this digit as candidate, otherwise, we cannot pick this digit
        # if there is a tie, then try two and compare
        cache = {}
        m, n = len(nums1), len(nums2)

        def find1D(nums, k):
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def helper(ii, jj, k):
            if (ii, jj, k) in cache:
                return cache[(ii,jj,k)]

            if k == 0:
                return []
            if k == 1:
                # return the largest digit
                res = [max(nums1[ii:] + nums2[jj:])]
                cache[(ii,jj,k)] = res
                return res

            if ii == m:
                # only find from nums2 with k
                if n-jj == k:
                    res = nums2[jj:]
                    cache[(ii,jj,k)] = res
                    return res
            elif jj == n:
                # only find from nums1 with k
                if m-ii == k:
                    res = nums1[ii:]
                    cache[(ii,jj,k)] = res
                    return res

            max1 = [-1, -1]  # max of valid candidates of nums1
            max2 = [-1, -1]  # max of valid candidates of nums2
            for i in range(ii, m):
                # compute remaining digits if we pick nums1[i]
                if (m-i-1) + (n-jj) >= k-1:
                    if nums1[i] > max1[0]:
                        max1 = [nums1[i], i]
            for j in range(jj, n):
                # compute remaining digits if we pick nums2[j]
                if (n-j-1) + (m-ii) >= k-1:
                    if nums2[j] > max2[0]:
                        max2 = [nums2[j], j]
            # pick the largest from two candidates
            res = []
            if max1[0] > max2[0]:
                val, i = max1
                res = [val] + helper(i+1, jj, k-1)
            elif max1[0] < max2[0]:
                val, j = max2
                res = [val] + helper(ii, j+1, k-1)
            else: # tie, try both
                val, i = max1
                res1 = [val] + helper(i+1, jj, k-1)
                val, j = max2
                res2 = [val] + helper(ii, j+1, k-1)
                res = max(res1, res2)
            cache[(ii,jj,k)] = res
            return res
        return helper(0, 0, k)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        nums1 = [3, 4, 6, 5]
        nums2 = [9, 1, 2, 5, 8, 3]
        k = 5
        self.assertEqual(self.s.maxNumber(nums1, nums2, k), [9, 8, 6, 5, 3])
        nums1 = [6, 7]
        nums2 = [6, 0, 4]
        k = 5
        self.assertEqual(self.s.maxNumber(nums1, nums2, k), [6, 7, 6, 0, 4])
        nums1 = [3, 9]
        nums2 = [8, 9]
        k = 3
        self.assertEqual(self.s.maxNumber(nums1, nums2, k), [9, 8, 9])
        nums1 = [4,6,9,1,0,6,3,1,5,2,8,3,8,8,4,7,2,0,7,1,9,9,0,1,5,9,3,9,3,9,7,3,0,8,1,0,9,1,6,8,8,4,4,5,7,5,2,8,2,7,7,7,4,8,5,0,9,6,9,2]
        nums2 = [9,9,4,5,1,2,0,9,3,4,6,3,0,9,2,8,8,2,4,8,6,5,4,4,2,9,5,0,7,3,7,5,9,6,6,8,8,0,2,4,2,2,1,6,6,5,3,6,2,9,6,4,5,9,7,8,0,7,2,3]
        k = 60
        res = [9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,6,8,8,4,4,5,7,5,2,8,2,7,7,7,4,8,5,0,9,6,9,2,0,2,4,2,2,1,6,6,5,3,6,2,9,6,4,5,9,7,8,0,7,2,3]
        self.assertEqual(self.s.maxNumber(nums1, nums2, k), res)
        nums1 = [2,1,2,0,2,1,1,2,0,1,0,0,1,1,1,0,1,2,0,0,1,2,2,1,2,2,2,0,1,1,0,0,0,2,0,0,1,0,0,2,2,1,1,1,1,2,0,2,0,2,2,1,0,1,1,1,1,0,0,0,0,1,0,2,1,2,2,0,2,0,2,2,2,2,0,0,2,1,2,0,0,1,1,0,1,2,1,0,0,0,0,0,0,2,0,2,2,2,2,1,1,0,1,2,1,2,1,0,0,0,1,0,2,0,1,1,1,2,0,0,1,1,0,1,0,0,0,0,2,2,1,0,0,1,1,1,1,0,2,1,1,2,1,2,1,0,1,1,2,1,1,1,0,2,1,0,0,0,2,1,1,1,1,0,1,1,1,0,0,0,1,1,2,0,0,1,1,0,2,2,2,1,2,2,0,2,2,2,2,2,1,0,0,0,2,1,0,1,0,1]
        nums2 = [1,2,1,2,2,0,1,2,2,1,2,1,2,2,1,2,1,1,1,1,2,0,0,0,2,2,0,2,0,0,1,0,1,1,1,0,2,2,2,0,1,1,1,0,2,2,1,2,0,0,2,0,1,1,0,1,0,0,0,2,0,1,0,1,2,1,1,0,2,2,0,2,0,0,0,1,0,2,2,0,2,0,0,2,1,0,2,1,2,2,1,2,0,1,1,0,2,0,0,1,1,2,0,2,1,0,2,1,0,0,0,1,1,1,2,2,1,1,0,1,1,2,1,0,2,0,1,1,2,0,1,2,2,1,2,1,2,2,1,1,2,1,2,1,2,0,0,0,0,2,1,1,1,0,2,2,0,1,2,2,2,1,2,1,0,2,2,0,1,0,2,1,2,2,1,0,1,1,0,2,0,1,1,2,0,0,0,2,0,1,0,1,1,2,0,1,2,1,2,0]
        k = 400
        self.s.maxNumber(nums1, nums2, k)

if __name__ == "__main__":
    unittest.main()
