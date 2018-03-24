

# beats 52.33%
# python KeyOrderedDict
from bisect import bisect_right
from collections import defaultdict
class MyCalendarThree(object):

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
        res = 0
        for key in self.keys:
            booked += self.events[key]
            res = max(res, booked)
        return res
    
    def update_dict(self, key, value):
        # value could be -1 or +1
        if key not in self.events:
            idx = bisect_right(self.keys, key)
            if not (idx > 0 and self.keys[idx-1] == key):  # not duplicate
                self.keys.insert(idx, key)
        self.events[key] += value
        # print(self.keys)
        # print(self.events)


# Your MyCalendarThree object will be instantiated and called as such:
obj = MyCalendarThree()
print(obj.book(10,20))
print(obj.book(50,60))
print(obj.book(10,40))
print(obj.book(5,15))