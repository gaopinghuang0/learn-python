import unittest

# beats 8.91%
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # idea: foreach i, calculate the distance between i and j
        # then select 2 out of them, the order matters
        n = len(points)
        if n < 3:
            return 0
        res = 0
        dist_dict = {}
        for i in range(n):
            dist_count = {}
            for j in range(n):
                if i == j:
                    continue
                elif (i,j) in dist_dict:
                    dist = dist_dict[(i,j)]
                else:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    dist = (x1-x2)**2 + (y1-y2)**2
                    dist_dict[(i,j)] = dist
                    dist_dict[(j,i)] = dist
                if dist in dist_count:
                    dist_count[dist] += 1
                else:
                    dist_count[dist] = 1
            for dist, count in dist_count.items():
                res += count * (count-1)
        return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.numberOfBoomerangs([[0,0],[1,0],[2,0]]), 2)


if __name__ == "__main__":
    unittest.main()
