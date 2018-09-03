import unittest

# beats 85.07%
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # idea: use two stacks
        def compress(S):
            if not S:
                return []
            stack = []
            for s in S:
                if s == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(s)
            return stack
            
        return compress(S) == compress(T)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # S = "ab#c"
        # T = "ad#c"
        # self.assertEqual(self.s.backspaceCompare(S, T), True)
        # S = "ab##"
        # T = "c#d#"
        # self.assertEqual(self.s.backspaceCompare(S, T), True)
        # S = "a##c"
        # T = "#a#c"
        # self.assertEqual(self.s.backspaceCompare(S, T), True)
        # S = "a#c"
        # T = "b"
        # self.assertEqual(self.s.backspaceCompare(S, T), False)
        S = "y#fo##f"
        T = "y#f#o##f"
        self.assertEqual(self.s.backspaceCompare(S, T), True)


if __name__ == "__main__":
    unittest.main()
