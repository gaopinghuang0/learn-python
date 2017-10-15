
from collections import Counter
class Solution(object):
  def leastBricks(self, wall):
    """
    :type wall: List[List[int]]
    :rtype: int
    """
    c = Counter()
    for row in wall:
      t = 0
      for x in row[:-1]:
        t += x
        c[t] += 1
    ans = c.most_common(2)
    return len(wall) if len(ans) <= 1 else len(wall) - ans[1][1]
