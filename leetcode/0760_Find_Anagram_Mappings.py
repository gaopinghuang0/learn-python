import unittest

# beats 100%
class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        indice = {v:i for i,v in enumerate(B)}
        return [indice[v] for v in A]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        A = [12, 28, 46, 32, 50]
        B = [50, 12, 32, 46, 28]
        self.assertEqual(self.s.anagramMappings(A, B), [1, 4, 3, 2, 0])


if __name__ == "__main__":
    unittest.main()
