import unittest


# Credit: https://discuss.leetcode.com/topic/22476/16-18-lines-python-30-lines-c
from collections import defaultdict
class Solution(object):
  def alienOrder(self, words):
    """
    :type words: List[str]
    :rtype: str
    """
    pre, suc = defaultdict(set), defaultdict(set)
    for pair in zip(words, words[1:]):
      for a, b in zip(*pair):
        if a != b:
          suc[a].add(b)
          pre[b].add(a)
          break
      if a == b and len(pair[0]) > len(pair[1]):  # for case: ['wrt', 'wr'] -> ''
        return ''
    chars = set(''.join(words))
    free = chars - set(pre)
    order = ''
    while free:
      a = free.pop()
      order += a
      for b in suc[a]:
        pre[b].discard(a)
        if not pre[b]:
          free.add(b)
    return order * (set(order) == chars)  # str * (0 or 1) -> '' or str



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    print(self.s.alienOrder(['wrt', 'wr', 'et']))
    print(self.s.alienOrder(['wr', 'wrt']))
    print(self.s.alienOrder(['wrt', 'wr']))
    print(self.s.alienOrder(["za","zb","ca","cb"]))
    print(self.s.alienOrder(["za","za"]))
    print(self.s.alienOrder(["z","z"]))


if __name__ == "__main__":
  unittest.main()
