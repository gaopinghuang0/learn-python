import unittest


# beats 79.22%
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        memo = {}
        n = len(s)
        def is_valid(part):
            # '0' must be a single part, not leading zeros
            if len(part) > 1 and part[0] == '0':
                return False
            return int(part) <= 255

        def helper(idx, k):
            if (idx, k) in memo:
                return memo[(idx, k)]
            if idx >= n or k <= 0:
                return []
            if k == 1:
                part = s[idx:]
                if is_valid(part):
                    memo[(idx, k)] = [part]
                    return [part]
                else:
                    memo[(idx, k)] = []
                    return []
            if n - idx > k*3:
                memo[(idx,k)] = []
                return []
            elif n - idx == k*3:  # split every three digits
                ip = []
                for i in range(idx, n, 3):
                    part = s[i:i+3]
                    if is_valid(part):
                        ip.append(part)
                    else:
                        memo[(idx,k)] = []
                        return []
                ip = '.'.join(ip)
                memo[(idx,k)] = [ip]
                return [ip]
            else:
                ip = set()
                for i in range(1,4):
                    first = s[idx:i+idx]
                    if is_valid(first):
                        rest = helper(i+idx, k-1)
                        if rest:
                            for part in rest:
                                ip.add(first+'.'+part)
                memo[(idx, k)] = list(ip)
                return list(ip)

        helper(0, 4)
        return memo.get((0, 4), [])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def my_equal(self, list1, list2):
        self.assertEqual(set(list1), set(list2))

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.my_equal(self.s.restoreIpAddresses("25525511135"), ["255.255.11.135", "255.255.111.35"])
        self.my_equal(self.s.restoreIpAddresses("255255111352"), [])
        self.my_equal(self.s.restoreIpAddresses("255255111235"), ["255.255.111.235"])
        self.my_equal(self.s.restoreIpAddresses("1111"), ["1.1.1.1"])
        self.my_equal(self.s.restoreIpAddresses("12111"), ["1.2.1.11","1.2.11.1","1.21.1.1","12.1.1.1"])
        groud_truth = ["1.2.1.111","1.2.11.11","1.2.111.1","1.21.1.11","1.21.11.1","1.211.1.1","12.1.1.11","12.1.11.1","12.11.1.1","121.1.1.1"]
        my_res = self.s.restoreIpAddresses("121111")
        self.my_equal(groud_truth, my_res)
        self.my_equal(self.s.restoreIpAddresses("010010"), ["0.10.0.10","0.100.1.0"])
        
if __name__ == "__main__":
    unittest.main()
