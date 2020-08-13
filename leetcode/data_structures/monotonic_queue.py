# 特殊数据结构：单调队列
# https://github.com/labuladong/fucking-algorithm/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E7%B3%BB%E5%88%97/%E5%8D%95%E8%B0%83%E9%98%9F%E5%88%97.md
# For leetcode 239 Sliding Window Maximum

# Similarly, monotonic stack.
# leetcode 84 Largest rectangle in Histogram.

# 就是一个「队列」，只是使用了一点巧妙的方法，使得队列中的元素单调递增（或递减）
# 这个数据结构有什么用？可以解决滑动窗口的一系列问题。

from collections import deque

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
