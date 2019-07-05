# second idea from submission: use dict
# beats 99.84%.
import collections
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.query = []
        self.candidates = []
        self.history = collections.defaultdict(int)
        for s, time in zip(sentences, times):
            self.history[s] = time

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            s = ''.join(self.query)
            self.history[s] += 1
            self.candidates = []
            self.query = []
            return []

        if not self.query:
            self.candidates = [(-time, s) for s, time in self.history.items() \
                if s[0] == c]
            self.candidates.sort()
            self.candidates = [s for time, s in self.candidates]
        else:
            n = len(self.query)
            self.candidates = [s for s in self.candidates if len(s) > n and s[n] == c]

        self.query.append(c)
        return self.candidates[:3]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

### Test cases:
["AutocompleteSystem","input","input","input","input", "input", "input", "input", "input", "input", "input", "input"]
[[["i love you","island","iroman","i love leetcode"],[5,3,2,2]],["i"],[" "],["a"],["#"],["a"],["#"], ["i"], [" "], ["a"], ["#"], ["i"]]

# try to optimize first idea: use Trie
# beats 81.15%, basically the same.
# class AutocompleteSystem(object):

#     def __init__(self, sentences, times):
#         """
#         :type sentences: List[str]
#         :type times: List[int]
#         """
#         self.trie = {}
#         self.build_trie(sentences, times)
#         self.prefix = []
#         self.last = self.trie  # store the last result
    
#     def build_trie(self, sentences, times):
#         for sent, time in zip(sentences, times):
#             self.add_sentence(sent, time)
    
#     def add_sentence(self, sentence, time):
#         t = self.trie
#         for c in sentence:
#             if c not in t:
#                 t[c] = {}
#             t = t[c]
#         # mark the end of word and save the times
#         if '#' in t:
#             t['#'] += time
#         else:
#             t['#'] = time

#     def input(self, c):
#         """
#         :type c: str
#         :rtype: List[str]
#         """
#         if c == '#':
#             if c in self.last:
#                 self.last[c] += 1
#             else:
#                 self.last[c] = 1
#             self.prefix = []
#             self.last = self.trie
#             return []

#         self.prefix.append(c)
#         if c not in self.last:
#             self.last[c] = {}
#             self.last = self.last[c]
#             return []

#         self.last = self.last[c]
#         return self.find_hottest(self.last)
    
#     def find_hottest(self, last):
#         res = []
#         def dfs(pre, trie):
#             if not trie:
#                 return
#             for c in trie:
#                 if c == '#':
#                     res.append((-trie['#'], pre))
#                 else:
#                     dfs(pre+c, trie[c])
#         dfs('', last)
#         res.sort()
#         ans = []
#         prefix = ''.join(self.prefix)
#         for time, pre in res[:3]:
#             ans.append(prefix+pre)
#         return ans
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

# first idea: use Trie
# beats 81.64%
# class AutocompleteSystem(object):

#     def __init__(self, sentences, times):
#         """
#         :type sentences: List[str]
#         :type times: List[int]
#         """
#         self.trie = {}
#         self.build_trie(sentences, times)
#         self.prefix = []
#         self.last = self.trie  # store the last result
    
#     def build_trie(self, sentences, times):
#         for sent, time in zip(sentences, times):
#             self.add_sentence(sent, time)
    
#     def add_sentence(self, sentence, time):
#         t = self.trie
#         for c in sentence:
#             if c not in t:
#                 t[c] = {}
#             t = t[c]
#         # mark the end of word and save the times
#         if '#' in t:
#             t['#'] += time
#         else:
#             t['#'] = time

#     def input(self, c):
#         """
#         :type c: str
#         :rtype: List[str]
#         """
#         if c == '#':
#             self.add_sentence(''.join(self.prefix), 1)
#             self.prefix = []
#             self.last = self.trie
#             return []

#         self.prefix.append(c)
#         if not self.last:
#             return []
#         self.last = self.last.get(c, None)
#         if not self.last:
#             return []
#         return self.find_hottest(self.last)
    
#     def find_hottest(self, last):
#         res = []
#         def dfs(pre, trie):
#             if not trie:
#                 return
#             for c in trie:
#                 if c == '#':
#                     res.append((-trie['#'], pre))
#                 else:
#                     dfs(pre+c, trie[c])
#         dfs('', last)
#         res.sort()
#         ans = []
#         prefix = ''.join(self.prefix)
#         for time, pre in res[:3]:
#             ans.append(prefix+pre)
#         return ans
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)