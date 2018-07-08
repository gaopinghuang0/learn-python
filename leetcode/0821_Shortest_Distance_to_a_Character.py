import unittest

# beats 99.73%
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # idea: arr_of_index_interval of C
        intervals = []
        start = -1000
        for i, c in enumerate(S):
            if c == C:
                intervals.append((start, i))
                start = i
        intervals.append((start, 10000000))
        # print(intervals)
        res = []
        interval_indx = 0
        for i, c in enumerate(S):
            start, end = intervals[interval_indx]
            if i == end:
                interval_indx += 1
                res.append(0)
            else:
                res.append(min(i-start, end-i))
        return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        S = "loveleetcode"
        C = 'e'
        self.assertEqual(self.s.shortestToChar(S, C), [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])


if __name__ == "__main__":
    unittest.main()
