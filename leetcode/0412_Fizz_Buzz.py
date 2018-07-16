import unittest

# beats 98.43%
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n+1):
            if i % 15 == 0:
                s ='FizzBuzz'
            elif i % 3 == 0:
                s = 'Fizz'
            elif i % 5 == 0:
                s = 'Buzz'
            else:
                s = str(i)
            res.append(s)
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.fizzBuzz(15), [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz"
        ])


if __name__ == "__main__":
    unittest.main()
