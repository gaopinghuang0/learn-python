import unittest

# idea from Discuss, beats 36.30%
# https://leetcode.com/problems/range-addition/discuss/84225/Detailed-explanation-if-you-don't-understand-especially-%22put-negative-inc-at-endIndex+1%22
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        # idea from Discuss, 
        # https://leetcode.com/problems/range-addition/discuss/84225/Detailed-explanation-if-you-don't-understand-especially-%22put-negative-inc-at-endIndex+1%22
        # only updates start_index and end_index+1, then compute range sum,
        # i.e., accumulates previous sum to current position
        res = [0] * (length+1)

        for e in updates:
            res[e[0]] += e[2]
            res[e[1]+1] -= e[2]

        # range sum
        for i in range(1, length):
            res[i] += res[i-1]

        res.pop()
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        length = 5
        updates = [
            [1,  3,  2],
            [2,  4,  3],
            [0,  2, -2]
        ]
        self.assertEqual(self.s.getModifiedArray(length, updates), [-2, 0, 3, 5, 3])


if __name__ == "__main__":
    unittest.main()
