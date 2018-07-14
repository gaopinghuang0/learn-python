import unittest

# beats 100%
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        # idea: similar to a stack
        res = 0
        points = []
        for op in ops:
            if op == 'D':
                x = 2 * points[-1]                
                points.append(x)
                res += x
            elif op == '+':
                x = points[-1] + points[-2]
                points.append(x)
                res += x
            elif op == 'C':
                res -= points.pop()
            else:
                x = int(op)
                points.append(x)
                res += x
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.calPoints(["5","2","C","D","+"]), 30)
        self.assertEqual(self.s.calPoints(["5","-2","4","C","D","9","+","+"]), 27)


if __name__ == "__main__":
    unittest.main()
