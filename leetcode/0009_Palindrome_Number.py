import unittest


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # x might be negative, then False
        # note: should be done without extra space
        # I agree with one comment in the discussion of leetcode,
        # this problem is meaningless because we cannot do it without extra space
        # because even a constant variable uses some space
        # also, some solution uses a variable to store a half of the digits, which 
        # uses half of digits in x, only slightly better than converting to a string
        # Credit: https://discuss.leetcode.com/topic/8090/9-line-accepted-java-code-without-the-need-of-handling-overflow
        if (x<0 or (x%10 == 0 and x != 0)):
        	return False

        rev = 0
        while x > rev:
         	rev = rev*10 + x%10
         	x = x // 10
        return (x == rev) or (x == rev//10)  # even or odd digits





class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.isPalindrome(151), True)
        self.assertEqual(self.s.isPalindrome(1), True)
        self.assertEqual(self.s.isPalindrome(12), False)
        self.assertEqual(self.s.isPalindrome(123454321), True)
        self.assertEqual(self.s.isPalindrome(12345432), False)
        self.assertEqual(self.s.isPalindrome(1234554321), True)
        self.assertEqual(self.s.isPalindrome(0), True)
        self.assertEqual(self.s.isPalindrome(-1), False)
        self.assertEqual(self.s.isPalindrome(-121), False)
        self.assertEqual(self.s.isPalindrome(-120), False)
        self.assertEqual(self.s.isPalindrome(-2147483648), False)



if __name__ == "__main__":
    unittest.main()
