import unittest


# beats 100%
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        # idea: just a for loop
        num_line = 1
        total_width = 0
        for c in S:
            width = widths[ord(c)-97]
            if total_width + width > 100:
                num_line += 1
                total_width = width
            else:
                total_width += width
        return [num_line, total_width]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        S = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(self.s.numberOfLines(widths, S), [3,60])
        widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        S = "bbbcccdddaaa"
        self.assertEqual(self.s.numberOfLines(widths, S), [2,4])


if __name__ == "__main__":
    unittest.main()
