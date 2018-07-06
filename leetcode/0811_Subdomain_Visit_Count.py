import unittest

# beats 100%
import collections
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # idea: use a dict
        count_dict = collections.defaultdict(int)
        for pair in cpdomains:
            count, domain = pair.split(' ')
            count = int(count)
            domains = domain.split('.')
            for i in range(len(domains)):
                count_dict['.'.join(domains[i:])] += count
        return [str(v)+' '+k for k, v in count_dict.items()]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def my_equal(self, arr1, arr2):
        self.assertEqual(set(arr1), set(arr2))

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.my_equal(self.s.subdomainVisits(["9001 discuss.leetcode.com"]), ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"])
        self.my_equal(self.s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]), ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"])


if __name__ == "__main__":
    unittest.main()
