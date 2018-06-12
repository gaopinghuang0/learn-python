import unittest

# idea from Submission
# optimize, cache the results, beats 100.00%
class Solution:
    nums = [1]
    idx = [0,0,0]  # for t2, t3, t5
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        t2, t3, t5 = Solution.idx
        while len(Solution.nums) < n:
            m = min(Solution.nums[t2]*2, Solution.nums[t3]*3, Solution.nums[t5]*5)
            Solution.nums.append(m)
            while Solution.nums[t2] * 2 <= m:
                t2 += 1
            while  Solution.nums[t3] * 3 <= m:
                t3 += 1
            while Solution.nums[t5] * 5 <= m:
                t5 += 1
        Solution.idx = [t2,t3,t5]
        return Solution.nums[n-1]

# beats 39.41%
class Solution_V1:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # suppose the current max ugly number is M, then we find T2 so that T2 is the first num in the array with T2 * 2 > M
        # similarly, we have T3 and T5
        primes = [2,3,5]
        t2 = t3 = t5 = 0
        nums = [1]
        i = 0
        for _ in range(n-1):
            m = min(nums[t2]*2, nums[t3]*3, nums[t5]*5)
            nums.append(m)
            while nums[t2] * 2 <= m:
                t2 += 1
            while nums[t3] * 3 <= m:
                t3 += 1
            while nums[t5] * 5 <= m:
                t5 += 1
        return nums[-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.nthUglyNumber(1), 1)
        self.assertEqual(self.s.nthUglyNumber(10), 12)
        self.assertEqual(self.s.nthUglyNumber(9), 10)
        self.assertEqual(self.s.nthUglyNumber(11), 15)


if __name__ == "__main__":
    unittest.main()
