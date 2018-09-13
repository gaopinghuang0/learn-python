import unittest


# beats 91.59%
class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        # idea from Discuss: O(n)
        # Credit: https://leetcode.com/problems/k-empty-slots/discuss/107931/JavaC++-Simple-O(n)-solution
        # use an array days in which days[i] means the blooming day of flower at position i+1
        # then find a subarray days[left, left+1, ..., left+k-1, right] which satisfies:
        # for any i = left+1, ..., left+k-1, days[left] < days[i] && days[i] > days[right]
        # in other words, flowers at position left and right bloom earlier than the flowers inbetween
        n = len(flowers)
        days = [0] * n
        for ith_day, flower_at_x in enumerate(flowers):
            days[flower_at_x-1] = ith_day
        # use a sliding window of length k
        left, right = 0, k+1
        i = 0
        res = float('inf')
        while right < n:
            while i < n and days[left] < days[i] and days[right] < days[i]:
                i += 1
            if i == right:  # a valid i
                res = min(res, max(days[left], days[right]))
            left = i
            right = i + k + 1
            i += 1
        return -1 if res == float('inf') else res + 1

# another faster solution from Submission
import math
class SolutionFaster(object):
        
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        min_buckets = [float('inf')] * int(math.ceil(len(flowers)/float(k+1)))
        max_buckets = [-(float('inf')-1)] * int(math.ceil(len(flowers)/float(k+1)))
        
        
        #print min_buckets, max_buckets
        
        for day, pos in enumerate(flowers):
            bucket_idx = (pos-1)/(k+1)
            if pos < min_buckets[bucket_idx]:
                min_buckets[bucket_idx] = pos
                if bucket_idx > 0 and pos - max_buckets[bucket_idx-1] == k+1:
                    return day+1
            if pos > max_buckets[bucket_idx]:
                max_buckets[bucket_idx] = pos
                if bucket_idx+1 < len(min_buckets) and min_buckets[bucket_idx+1] - pos == k+1:
                    return day+1
        
        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.kEmptySlots([1,3,2], 1), 2)
        self.assertEqual(self.s.kEmptySlots([1,2,3], 1), -1)


if __name__ == "__main__":
    unittest.main()
