import unittest

from collections import defaultdict
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        stack = []
        last_time = 0
        for log in logs:
            _id, task, time = log.split(":")
            _id, time = int(_id), int(time)

            if task == 'start':
                if stack:
                    ans[stack[-1]] += time - last_time
                stack.append(_id)
                last_time = time
            else:
                ans[stack.pop()] += time - last_time + 1
                last_time = time + 1

        return ans







class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        logs = ["0:start:0",
             "1:start:2",
             "1:end:5",
             "0:end:6"]
        self.assertEqual(self.s.exclusiveTime(2, logs), [3, 4])
        logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]      
        self.assertEqual(self.s.exclusiveTime(1, logs), [8])
        logs = ["0:start:0","1:start:4","2:start:8","3:start:12","4:start:17","4:end:711","3:end:714","2:end:718","5:start:722","6:start:723","6:end:726","7:start:728","8:start:733","8:end:736","7:end:738","5:end:742","1:end:747","0:end:749"]
        self.assertEqual(self.s.exclusiveTime(9, logs), [8])



if __name__ == "__main__":
    unittest.main()
