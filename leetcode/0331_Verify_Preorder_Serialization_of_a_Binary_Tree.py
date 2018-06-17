import unittest

# beats 62.11%
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # idea: use a stack
        # also record the number of children for each node
        stack = []
        nodes = preorder.split(',')
        n = len(nodes)
        for i, val in enumerate(nodes):
            if val != '#':
                stack.append((val, 0))
            else:
                while stack:
                    node, cnt = stack.pop()
                    cnt += 1
                    if cnt == 2:
                        continue
                    else:
                        stack.append((node, cnt))
                        break
                if not stack and i < n-1:
                    return False
        return len(stack) == 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"), True)
        self.assertEqual(self.s.isValidSerialization(""), False)
        self.assertEqual(self.s.isValidSerialization("1,#"), False)
        self.assertEqual(self.s.isValidSerialization("9,#,#,1"), False)
        self.assertEqual(self.s.isValidSerialization("9,#,#,1"), False)
        self.assertEqual(self.s.isValidSerialization("9,#,#"), True)
        self.assertEqual(self.s.isValidSerialization("9,#,3,#,#"), True)
        self.assertEqual(self.s.isValidSerialization("9,3,#,#,4,#,#"), True)
        self.assertEqual(self.s.isValidSerialization("#"), True)
        self.assertEqual(self.s.isValidSerialization("9,9,#,#,9,#,#"), True)
        self.assertEqual(self.s.isValidSerialization("9,3,4,#,#,1,#,#,#,2,#,6,#,#"), False)


if __name__ == "__main__":
    unittest.main()
