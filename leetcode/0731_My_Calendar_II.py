
# beats 96.06%
from bisect import bisect_left
class MyCalendarTwo(object):

    def __init__(self):
        self.timeline = [-1, 10**9+1]
        self.bookings = [0,0]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        i = bisect_left(self.timeline, start)
        j = bisect_left(self.timeline, end)
        # print(start,end)
        # print(["%02d"%x for x in self.timeline])
        # print(["%02d"%x for x in self.bookings])
        if self.timeline[i] != start and self.bookings[i-1] == 2:
            return False
        for idx in range(i, j):
            if self.bookings[idx] == 2:
                return False

        if self.timeline[i] != start:
            self.timeline.insert(i, start)
            self.bookings.insert(i, self.bookings[i-1])
            j += 1

        if self.timeline[j] != end:
            self.timeline.insert(j, end)
            self.bookings.insert(j, self.bookings[j-1])

        for idx in range(i, j):
            self.bookings[idx] += 1

        return True



# time limit exceeded
# python KeyOrderedDict
from bisect import bisect_right
from collections import defaultdict
class MyCalendarTwoSlow(object):

    def __init__(self):
        self.keys = []   # maintain sorted keys
        self.events = defaultdict(int)

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # idea: use a KeyOrderedDict (similar to TreeMap in Java) as timeline
        # increase one to start a on-going event,
        # decrease one to end a on-going event
        self.update_dict(start, 1)
        self.update_dict(end, -1)
        booked = 0
        for key in self.keys:
            booked += self.events[key]
            if booked == 3:
                self.update_dict(start, -1)
                self.update_dict(end, 1)
                return False
        return True
    
    def update_dict(self, key, value):
        # value could be -1 or +1
        if key not in self.events:
            idx = bisect_right(self.keys, key)
            if not (idx > 0 and self.keys[idx-1] == key):  # not duplicate
                self.keys.insert(idx, key)
        self.events[key] += value
        # print(self.keys)
        # print(self.events)



# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo()
for start, end in [[36,41],[28,34],[40,46],[10,18],[4,11],[25,34],[36,44],[32,40],[34,39],[40,49]]:
    print(obj.book(start, end))
