import unittest

from collections import deque
from typing import List

class MonotonicQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, n: int):
        """Remove the values in the queue that are smaller than n.
        
        For example: initial queue [5,3,2,1], n=4
        result queue:  [5,4]
        """
        while self.queue and self.queue[-1] < n:
            self.queue.pop()
        self.queue.append(n)

    def max(self) -> int:
        return self.queue[0]

    def pop(self, n: int):
        "Only pop if the queue front matches n"
        if self.queue and self.queue[0] == n:
            self.queue.popleft()

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Use a monotonic queue
        window = MonotonicQueue()
        res = []
        for i, num in enumerate(nums):
            if i < k - 1:
                window.push(num)
            else:
                window.push(num)
                res.append(window.max())
                window.pop(nums[i-k+1])
        return res


# beats 39.12%
class Solution_1(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # k is always valid
        if not nums:
            return []

        n = len(nums)
        counter = {}
        for x in nums[:k]:
            counter[x] = counter.get(x, 0) + 1
        cur_max = max(nums[:k])
        res = [cur_max]
        for left in range(1, n-k+1):
            old = nums[left-1]            
            new = nums[left+k-1]
            counter[new] = counter.get(new, 0) + 1
            counter[old] -= 1
            if counter[old] <= 0:
                del counter[old]
                if old == cur_max:
                    # need to find new cur_max
                    cur_max = max(counter.keys())
            if new >= cur_max:
                cur_max = new
            res.append(cur_max)
        return res


class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    self.assertEqual(self.s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7])
    nums = [-95,92,-85,59,-59,-14,88,-39,2,92,94,79,78,-58,37,48,63,-91,91,74,-28,39,90,-9,-72,-88,-72,93,38,14,-83,-2,21,4,-75,-65,3,63,100,59,-48,43,35,-49,48,-36,-64,-13,-7,-29,87,34,56,-39,-5,-27,-28,10,-57,100,-43,-98,19,-59,78,-28,-91,67,41,-64,76,5,-58,-89,83,26,-7,-82,-32,-76,86,52,-6,84,20,51,-86,26,46,35,-23,30,-51,54,19,30,27,80,45,22]
    k = 10
    res = [92,94,94,94,94,94,94,94,94,94,94,91,91,91,91,91,91,91,93,93,93,93,93,93,93,93,93,93,63,100,100,100,100,100,100,100,100,100,100,59,48,87,87,87,87,87,87,87,87,87,100,100,100,100,100,100,100,100,100,100,78,78,78,78,78,83,83,83,83,83,83,86,86,86,86,86,86,86,86,86,86,84,84,84,54,54,54,54,80,80,80]
    self.assertEqual(self.s.maxSlidingWindow(nums, k), res)

if __name__ == "__main__":
  unittest.main()
