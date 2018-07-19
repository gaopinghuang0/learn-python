import unittest

import itertools
# optimize, idea from Submission, beats 58.90%
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        L = [i.lower()+i.upper() if i.isalpha() else i for i in S]
        return ["".join(i) for i in itertools.product(*L)]


# beats 33.86%
class Solution_V1(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # idea: recursive
        if not S:
            return ['']
        ans = set()
        first = S[0]
        for rest in self.letterCasePermutation(S[1:]):
            if '0' <= first <= '9':
               ans.add(first + rest)
            else:
                ans.add(first.lower() + rest)
                ans.add(first.upper() + rest)
        return list(ans)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def my_list_equal(self, list1, list2):
        self.assertEqual(set(list1), set(list2))

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        ans = ["a1b2", "a1B2", "A1b2", "A1B2"]
        self.my_list_equal(self.s.letterCasePermutation("a1b2"), ans)
        ans = ["3z4", "3Z4"]
        self.my_list_equal(self.s.letterCasePermutation("3z4"), ans)
        ans = ["12345"]
        self.my_list_equal(self.s.letterCasePermutation("12345"), ans)
        self.my_list_equal(self.s.letterCasePermutation(""), [''])


if __name__ == "__main__":
    unittest.main()
