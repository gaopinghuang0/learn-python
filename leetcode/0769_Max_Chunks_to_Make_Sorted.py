import unittest

# beats 21.88%
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # idea: use the max val of the chunk end_index
        max_val = 0
        res = 0
        for i, val in enumerate(arr):
            if val > max_val:
                max_val = val
            if i == max_val:
                res += 1
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        arr = [4,3,2,1,0]
        self.assertEqual(self.s.maxChunksToSorted(arr), 1)
        arr = [1,0,2,3,4]
        self.assertEqual(self.s.maxChunksToSorted(arr), 4)
        arr = [2,0,1,3,4]
        self.assertEqual(self.s.maxChunksToSorted(arr), 3)
        arr = [0,3,1,2,4]
        self.assertEqual(self.s.maxChunksToSorted(arr), 3)

if __name__ == "__main__":
    unittest.main()
