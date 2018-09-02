import unittest

# beats 95.22%
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # idea: compute the max distance between nearby two seats
        max_dist = 0
        prev = 0
        n = len(seats)
        i = 0
        while i < n and seats[i] == 0:
            i += 1
        prev = i
        start = prev
        while i < n:
            if seats[i]:
                max_dist = max(max_dist, i-prev)
                prev = i
            i += 1
        return max(start, max_dist//2, n-1-prev)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.maxDistToClosest([1,0,0,0,1,0,1]), 2)
        self.assertEqual(self.s.maxDistToClosest([1,0,0,0]), 3)
        self.assertEqual(self.s.maxDistToClosest([0,1]), 1)


if __name__ == "__main__":
    unittest.main()
