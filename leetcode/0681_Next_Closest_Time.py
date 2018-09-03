import unittest

# idea from Discuss, beats 100%
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        # idea: start from the back and try smallest digit
        # adapted from https://leetcode.com/problems/next-closest-time/discuss/166221/Easy-to-understand-Python-Beats-100
        def is_valid(h, m):
            return int(h) < 24 and int(m) < 60

        s = time[:2] + time[3:]  # input is always valid, 'ab:cd'
        cand = set(s)
        if len(cand) == 1:
            return time

        sorted_cand = sorted(list(cand))
        for i in range(3, -1, -1):
            for c in sorted_cand:
                if c > s[i]:
                    res = s[:i] + c + sorted_cand[0] * (3-i)
                    if is_valid(res[:2], res[2:]):
                        return res[:2] + ':' + res[2:]
        # the only valid and smallest digit is s[0], such as '23:59', '09:49'
        return s[0] * 2 + ':' + s[0] * 2



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.nextClosestTime('19:34'), '19:39')
        self.assertEqual(self.s.nextClosestTime('23:59'), '22:22')
        self.assertEqual(self.s.nextClosestTime('09:49'), '00:00')


if __name__ == "__main__":
    unittest.main()
