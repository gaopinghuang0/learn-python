

# idea: two hashmap with OrderedDict, beats 17.02%
# my idea is exactly the same as this link:
# https://leetcode.com/problems/lfu-cache/discuss/139729/Concise-Python-using-OrderedDict
import collections
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_value_count = {}  # {key: [value, count]}
        self.freq = collections.defaultdict(collections.OrderedDict)
        self.min_count = 0

    def _touch(self, key):
        assert(key in self.key_value_count)
        cur_count = self.key_value_count[key][1]
        self.freq[cur_count].pop(key)
        self.key_value_count[key][1] += 1  # increase count
        self.freq[cur_count+1][key] = True  # add to next freq bucket
        # update min_count
        if len(self.freq[self.min_count]) == 0:
            self.min_count += 1

    def _evict(self):
        # since we will only evict when we put a new key, which will make min_count as 1 later
        assert(self.min_count in self.freq)
        # OrderedDict popitem(True) in LIFO order False in FIFO order
        key, value = self.freq[self.min_count].popitem(False)
        del self.key_value_count[key]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_value_count:
            return -1
        value, count = self.key_value_count.get(key)
        self._touch(key)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0: return
        if key in self.key_value_count:
            self.key_value_count[key][0] = value
            self._touch(key)
        else:
            if len(self.key_value_count) == self.capacity:
                self._evict()
            self.key_value_count[key] = [value, 1]
            self.freq[1][key] = True
            self.min_count = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)