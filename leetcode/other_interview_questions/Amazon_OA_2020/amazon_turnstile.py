"""
Amazon OA Turnstile
https://leetcode.com/discuss/interview-question/798231/
"""

import unittest
from typing import List
from collections import OrderedDict, deque

class Solution:
    def amazon_turnstile(self, numCustomers: int, arrTime: List[int], direction: List[int]) -> List[int]:
        i = 0
        currTime = arrTime[0]
        lastDir = None
        enter = deque()
        exit = deque()
        res = [-1] * numCustomers
        while i < numCustomers:
            while i < numCustomers and arrTime[i] <= currTime:
                if direction[i] == 0:
                    enter.append(i)
                else:
                    exit.append(i)
                i += 1
            
            if enter or exit:
                # find a proper one and delete
                if lastDir is None:  # first pick the one that exits
                    to_move = None
                    if exit:
                        to_move = exit.popleft()
                        lastDir = 1
                    else:
                        to_move = enter.popleft()
                        lastDir = 0
                elif lastDir == 0:
                    if enter:
                        to_move = enter.popleft()
                    else:
                        to_move = exit.popleft()
                        lastDir = 1
                else:
                    if exit:
                        to_move = exit.popleft()
                    else:
                        to_move = enter.popleft()
                        lastDir = 0
                res[to_move] = currTime
                currTime += 1
            else:
                # nobody is waiting
                if arrTime[i] - currTime > 1:
                    lastDir = None
                currTime = arrTime[i]
        while enter or exit:
            # find a proper one and delete
            if lastDir is None:  # first pick the one that exits
                to_move = None
                if exit:
                    to_move = exit.popleft()
                    lastDir = 1
                else:
                    to_move = enter.popleft()
                    lastDir = 0
            elif lastDir == 0:
                if enter:
                    to_move = enter.popleft()
                else:
                    to_move = exit.popleft()
                    lastDir = 1
            else:
                if exit:
                    to_move = exit.popleft()
                else:
                    to_move = enter.popleft()
                    lastDir = 0
            res[to_move] = currTime
            currTime += 1
        return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        # case 1
        numCustomers = 4
        arrTime = [0, 0, 1, 5]
        direction = [0, 1, 1, 0]
        result = [2, 0, 1, 5]
        self.assertEqual(self.s.amazon_turnstile(numCustomers, arrTime, direction), result)

        # case 2
        numCustomers = 5
        arrTime = [0, 1, 1, 3, 3]
        direction = [0, 1, 0, 0, 1]
        result = [0, 2, 1, 4, 3]
        self.assertEqual(self.s.amazon_turnstile(numCustomers, arrTime, direction), result)

if __name__ == "__main__":
    unittest.main()