import unittest


# beats 35.51%
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # idea: use a stack to store the current string, if stack is empty, add to the ans
        ans = ''
        stack = []
        size = len(s)
        i = 0
        while i < size:
            if s[i].isdigit():
                j = i + 1
                while j < size and s[j].isdigit():
                    j += 1
                stack.append(int(s[i:j]))
                i = j
            elif s[i] == '[':
                j = i + 1
                while j < size and s[j].isalpha():
                    j += 1
                stack.append(s[i+1:j])
                i = j
            elif s[i] == ']':
                encoded = stack.pop()
                k = stack.pop()
                temp = encoded * k
                if stack:
                    encoded = stack.pop()
                    stack.append(encoded + temp)
                else:
                    ans += temp
                i += 1
            else:  # normal string
                j = i + 1
                while j < size and s[j].isalpha():
                    j += 1
                if stack:
                    encoded = stack.pop()
                    stack.append(encoded + s[i:j])
                else:
                    ans += s[i:j]
                i = j
        return ans



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
