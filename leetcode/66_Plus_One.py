import unittest


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # my own accepted solution: 42ms, beats 69.65%, maybe not accurate
        # num = int(''.join(map(str, digits))) + 1
        # return [int(i) for i in str(num)]

        # the fastest solution: 35ms, maybe not accurate
        for i in range(len(digits)-1, -1, -1):
          if digits[i] == 9:
            digits[i] = 0
          else:
            digits[i] += 1
            break
        if digits[0] == 0:
          digits.insert(0, 1)
        return digits
        


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # non-empty array with non-negative digits, no leading zero
        self.assertEqual(self.s.plusOne([0]), [1])
        self.assertEqual(self.s.plusOne([1]), [2])
        self.assertEqual(self.s.plusOne([9]), [1, 0])
        self.assertEqual(self.s.plusOne([1,9]), [2, 0])
        self.assertEqual(self.s.plusOne([9,9]), [1, 0, 0])
        self.assertEqual(self.s.plusOne([1,9,9]), [2, 0, 0])
        self.assertEqual(self.s.plusOne([9,9,9]), [1, 0, 0, 0])
        self.assertEqual(self.s.plusOne([1,0,9,9]), [1, 1, 0, 0])
        self.assertEqual(self.s.plusOne([1,0,9,0,9]), [1, 0, 9, 1, 0])


if __name__ == "__main__":
    unittest.main()
