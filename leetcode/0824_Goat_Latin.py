import unittest

# beats 80%
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        vowels = set('aeiouAEIOU')
        for i, word in enumerate(S.split(' '), 1):
            if word[0] in vowels:
                res.append(word + 'ma' + 'a'*i)
            else:
                res.append(word[1:]+word[0]+'ma'+'a'*i)
        return ' '.join(res)

        

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.toGoatLatin("I speak Goat Latin"), "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
        inp = "The quick brown fox jumped over the lazy dog"
        outp = "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
        self.assertEqual(self.s.toGoatLatin(inp), outp)



if __name__ == "__main__":
    unittest.main()
