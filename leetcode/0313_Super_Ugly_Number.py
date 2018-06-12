import unittest

# beats 48.66%
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        # idea similar to 0264_Ugly_Number_II
        idx = [0]*len(primes)  # idx for each prime p so that idx_p * p > the current largest ugly num
        nums = [1]
        for _ in range(n-1):
            m = min((nums[idx[i]]*prime for i, prime in enumerate(primes)))
            nums.append(m)
            for i, prime in enumerate(primes):
                while nums[idx[i]] * prime <= m:
                    idx[i] += 1
        return nums[-1]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.nthSuperUglyNumber(12, [2,7,13,19]), 32)
        self.assertEqual(self.s.nthSuperUglyNumber(1, [2,7,13,19]), 1)
        self.assertEqual(self.s.nthSuperUglyNumber(3, [2,7,13,19]), 4)
        self.assertEqual(self.s.nthSuperUglyNumber(4, [2,7,13,19]), 7)


if __name__ == "__main__":
    unittest.main()
