import unittest

# beats 55.63%
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # idea: iteration, use one line to handle duplicates
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i < len(l) and l[i] == n:  # handle duplicates, see explanation below
                        break
            ans = new_ans
        return ans
        # below is an explanation of this method by zjufisher from Discussion
        # Here is my understanding about the eliminate process.

        # After several times of append and other operations,
        # #here I just pay attention to one element, 2's position in the inner list
        # We get the current list like below:

        # [2,x,x,x]
        # [x,2,x,x]
        # [x,x,2,x]
        # [x,x,x,2]
        # Of course if we replace the "x" with other elements, there should be several other lists in each row,but the position of "2" should just be same,[0],[1],[2],[3] for each row.
        # The approach will traverse each list and insert the new element.
        # If the new element is "2", the current "for loop" will break.
        # Therefor,after the two loops,the "2" 's positions in the list should be:
        # [0,1]
        # [0,2],[1,2]
        # [0,3],[1,3],[2,3]
        # [0,4],[1,4],[2,4],[3,4]
        # It will actually cover all the situation of the two 2's distribution.

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    pass


if __name__ == "__main__":
  unittest.main()
