import unittest

# beats 99.89%
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        unique = set()
        for word in words:
            unique.add(''.join([morse_code[ord(c)-97] for c in word]))
        return len(unique)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]), 2)


if __name__ == "__main__":
    unittest.main()
