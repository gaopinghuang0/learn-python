import unittest

# beats 28.21%
from heapq import heappush, heappop
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # idea: maintain a queue as borders, start from two ends
        if not height:
            return 0

        n = len(height)
        visited = [0]*n
        hp = []
        for i in [0, n-1]:
            heappush(hp, (height[i], i))
            visited[i] = 1
        res = 0
        while hp:
            h, i = heappop(hp)
            for delta in (1, -1):
                x = i + delta
                if 0 <= x < n and not visited[x]:
                    res += max(0, h - height[x])
                    heappush(hp, (max(h, height[x]), x))
                    visited[x] = 1
        return res



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    self.assertEqual(self.s.trap(height), 6)


if __name__ == "__main__":
  unittest.main()
