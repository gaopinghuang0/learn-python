import unittest

# beats 55.54%
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # idea: use a stack, backwards
        n = len(temperatures)
        res = [0]*n
        stack = [(0,None)]
        for i in range(n-1, -1, -1):
            temp = temperatures[i]
            while stack and temp >= stack[-1][0]:
                stack.pop()
            if not stack:
                res[i] = 0
            else:
                res[i] = stack[-1][1]-i
            stack.append((temp, i))
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        self.assertEqual(self.s.dailyTemperatures(temperatures), [1, 1, 4, 2, 1, 1, 0, 0])
        temperatures = [89,62,70,58,47,47,46,76,100,70]
        self.assertEqual(self.s.dailyTemperatures(temperatures), [8,1,5,4,3,2,1,1,0,0])

if __name__ == "__main__":
    unittest.main()
