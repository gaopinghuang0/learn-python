import unittest


# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
import random
# suppose the celebrity is c, then every else should know c, but c knows nobody
celebrity = 4
def knows(a, b):
  global celebrity

  if a == celebrity:
    return False
  if b == celebrity:
    return True
  return random.randint(0,1)


class Solution(object):
  def findCelebrity(self, n):
    """
    :type n: int
    :rtype: int
    """
    # DAG, graph, if there is a celebrity, then all (n-1) edges should be inwards
    # idea: pick random one, and check whether others know it, if every one else does,
    # then check whether is knows any one else to see if it is celebrity
    # if not, check only the people who do not know the picked one, repeat the process
    candidate = 0
    for i in range(1, n):
      if knows(candidate, i):
        candidate = i
    for i in range(n):
      if i != candidate and (not knows(i, candidate) or knows(candidate, i)):
        return -1
    return candidate


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    global celebrity
    celebrity = 4
    self.assertEqual(self.s.findCelebrity(5), celebrity)

    celebrity = 3
    self.assertEqual(self.s.findCelebrity(5), celebrity)

    celebrity = -1
    self.assertEqual(self.s.findCelebrity(2), celebrity)


if __name__ == "__main__":
  unittest.main()
