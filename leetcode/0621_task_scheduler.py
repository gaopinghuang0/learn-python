import unittest

from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = Counter(tasks)
        i = 0
        big = counter.most_common(1)[0][1]
        while big > 1:
            for (task, c) in counter.most_common(n+1):
                counter[task] -= 1
            big = counter.most_common(1)[0][1]
            i += 1
            counter = +counter  # remove zero and negative counts

        if big == 1:
            return i * (n+1) + sum(counter.values())

        return i * (n+1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.leastInterval(['A','A','A','B','B','B'], 2), 8)
        self.assertEqual(self.s.leastInterval(['A','A','B'], 2), 4)
        self.assertEqual(self.s.leastInterval(['A','A','A','A','B','B'], 2), 10)
        self.assertEqual(self.s.leastInterval(['A','A'], 2), 4)


if __name__ == "__main__":
    unittest.main()
