import unittest

# beats 100%
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        # idea: try to imagine the laser can keep going up because it's mirror symmetrical
        # credit: https://leetcode.com/problems/mirror-reflection/discuss/141943/Easy-Understand-and-short-java-AC-solution
        up_dist = q
        times = 1
        while up_dist % p != 0:
            up_dist += q
            times += 1

        if times % 2 == 0:
            return 2
        elif (up_dist // p) % 2 == 0:  # even
            return 0
        else:
            return 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
    unittest.main()
