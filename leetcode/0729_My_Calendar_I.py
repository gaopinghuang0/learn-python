
# idea from Submissions, beats 98.72%
from bisect import bisect_left
class MyCalendar(object):

    def __init__(self):
        self.events = [(float('-inf'), float('-inf')), (float('inf'), float('inf'))]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        i = bisect_left(self.events, (start,end))
        if self.events[i][0] < end:
            return False
        if start < self.events[i-1][1]:
            return False
        self.events.insert(i, (start,end))
        return True


# beats 20%
class MyCalendar(object):

    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        n = len(self.events)
        i = 0
        while i < n and self.events[i][1] <= start:
            i += 1
        if i == n:
            self.events.append((start, end))
            return True
        if self.events[i][0] >= end:
            self.events.insert(i, (start,end))
            return True
        return False



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)