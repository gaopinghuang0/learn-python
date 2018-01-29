
# slow, beats 1.54%
from collections import Counter, defaultdict
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        # idea: use counter to compare the words
        # s must contain all chars of the desiring string in d
        if not s or not d:
            return ''

        s_counter = Counter(s)
        lookup = defaultdict(list)  # str_len: List[str]

        for t in d:
            lookup[len(t)].append(t)

        for key in sorted(lookup.keys(), reverse=True):
            for t in sorted(lookup[key]):
                t_counter = Counter(t)
                if len(t_counter - s_counter) == 0:
                    # furthur check if s can be converted to t
                    i, j = 0, 0
                    while i < len(s) and j < len(t):
                        if s[i] == t[j]:
                            i += 1
                            j += 1
                        else:
                            i += 1
                    if j == len(t):
                        return t
        return ''

sol = Solution()
print(sol.findLongestWord('abpcplea', ["ale","apple","monkey","plea"]))
print(sol.findLongestWord('abpcplea', ["a","b","c"]))


