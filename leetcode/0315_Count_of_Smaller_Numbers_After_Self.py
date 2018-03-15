import unittest


# idea from Discuss, beats 29.60%
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # idea from Discuss
        # the number of smaller elements to the right is exactly those who jump
        # from right to left during a stable sort
        # here, we just use a mergesort and count those jumps
        def sort(enum):
            half = len(enum) // 2
            if not half:
                return enum
            left, right = sort(enum[:half]), sort(enum[half:])
            # merge sort from the largest element (i.e., right to left)
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller



class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.countSmaller([5,2,6,1]), [2,1,1,0])
    


if __name__ == "__main__":
  unittest.main()
