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
    candidates = set(range(n))
    while len(candidates) > 0:
      pivot = candidates.pop()
      new_candidates = set([c for c in candidates if not knows(c, pivot)])
      if len(new_candidates) > 0:
        candidates = new_candidates
      else:  # check whether pivot is a celebrity
        unknowns = set([c for c in range(n) if c != pivot and not knows(c, pivot)])
        if len(unknowns) == 0:  # everyone knows pivot, pivot might be celebrity
          pivot_knows = [c for c in range(n) if c != pivot and knows(pivot, c)]
          if len(pivot_knows) == 0:  # pivot knows nobody
            return pivot
    return -1


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
