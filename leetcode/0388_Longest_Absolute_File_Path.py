import unittest

# idea from Discussion, beats 62.72%
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # require O(n) time complexity
        # the number of tabs is the depth
        # a good thing is that path_len will auto update if the new depth becomes smaller
        # since the lower depth will be updated before larger depth
        # in other words, path_len will always store the correct len for the current path
        maxlen = 0
        path_len = {0: 0}
        for s in input.splitlines():
            t = s.lstrip('\t')
            depth = len(s) - len(t)
            if '.' in t:  # is file
                maxlen = max(maxlen, path_len[depth] + len(t))
            else:
                path_len[depth+1] = path_len[depth] + len(t) + 1  # add '/' to the end
        return maxlen

# too complicated, not finished.
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # require O(n) time complexity
        # idea: use a stack
        stack = []
        n = len(input)
        i = 0
        res = ''
        while i < n:
            j = i
            while j < n and n[j] != '\\':
                j += 1
            if j < n:
                dir_or_file = n[i:j]
                if '.' in dir_or_file:  # is file
                    new_len = len(dir_or_file) + sum(map(len, stack))
                    if new_len > res:
                        res = new_len
                else:  # is dir

                stack.append(n[i:j])




class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
