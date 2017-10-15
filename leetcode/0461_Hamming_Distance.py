
# faster way
class Solution(object):
  def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x^y).count('1')

class Solution(object):
  def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return sum(i != j for i,j in zip(*map('{:032b}'.format, [x, y])))