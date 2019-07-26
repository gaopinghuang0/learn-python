# beats 83%
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # first split words in greedy way
        lines = []
        n = len(words)
        curr = 0
        i = 0
        line = []
        while i < n:
            word = words[i]
            if curr + len(word) > maxWidth:
                lines.append(line)
                curr = 0
                line = []
            else:
                line.append(word)
                curr += len(word) + 1
                i += 1
        if line:
            lines.append(line)
        # print(lines)

        res = []
        # justify each line except last line
        for line in lines[:-1]:
            res.append(self.even_justify(line, maxWidth))

        # left justify the last line
        res.append(self.left_justify(lines[-1], maxWidth))
        return res

    def even_justify(self, line, maxWidth):
        num = len(line)
        if num == 1:
            return self.left_justify(line, maxWidth)
        
        extra_spaces = maxWidth - len(' '.join(line))
        m = extra_spaces // (num - 1)
        k = extra_spaces % (num - 1)
        res = []
        for i in range(k):
            res.append(line[i] + ' ' * (m+1))
        for i in range(k, num-1):
            res.append(line[i] + ' ' * m)
        res.append(line[-1])
        return ' '.join(res)
    
    def left_justify(self, line, maxWidth):
        s = ' '.join(line)
        return s + (maxWidth - len(s)) * ' '


import unittest
class Test(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test0(self):
        sol = Solution()
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        expected = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
        self.assertEqual(self.sol.fullJustify(words, maxWidth), expected)

    def test1(self):
        sol = Solution()
        words = ["What","must","be","acknowledgment","shall","be"]
        maxWidth = 16
        expected = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        self.assertEqual(self.sol.fullJustify(words, maxWidth), expected)

    def test2(self):
        sol = Solution()
        words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
        maxWidth = 20
        expected = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]
        self.assertEqual(self.sol.fullJustify(words, maxWidth), expected)


if __name__ == "__main__":
    unittest.main()