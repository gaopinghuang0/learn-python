import unittest

# beats 69.44%
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # idea: Counter
        return [num for num, _ in collections.Counter(nums).most_common(k)]
        


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        nums = [1,1,1,2,2,3]
        k = 2
        self.assertEqual(self.s.topKFrequent(nums, k), [1,2])
        self.assertEqual(self.s.topKFrequent([1], 1), [1])


if __name__ == "__main__":
    unittest.main()
