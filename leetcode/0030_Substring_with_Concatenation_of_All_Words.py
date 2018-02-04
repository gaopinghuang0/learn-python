import unittest

# idea is the same as below, but code is shorter
# borrow from the submission
# beats 94.30%
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        s_len = len(s)
        w_size = len(words[0])
        total_size = len(words) * w_size
        counter = {}
        for word in words:
            counter[word] = counter.get(word, 0) + 1
        res = []
        for start in range(w_size):
            curr = {}
            end = start
            while start + total_size <= s_len:
                sub = s[end:end+w_size]
                end += w_size
                if sub not in counter:
                    curr = {}
                    start = end
                else:
                    curr[sub] = curr.get(sub, 0) + 1
                    while curr[sub] > counter[sub]:
                        curr[s[start:start+w_size]] -= 1
                        start += w_size
                    if start + total_size == end:
                        res.append(start)
        return res

# beats 49.00%
from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # note that words may contain duplicate words
        # idea2: loop w_size times, each time, maintain a window with length of total_size
        # my idea happened to be the same as the O(N) answer in the Discuss
        # https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13656/An-O(N)-solution-with-detailed-explanation
        if not s or not words:
            return []

        w_size = len(words[0])
        total_size = len(words) * w_size
        if len(s) < total_size:
            return []

        ctr = Counter(words)
        res = []
        # loop w_size times
        for i in range(w_size):
            left = i
            count = 0
            tmp_ctr = Counter()
            j = left
            while j + w_size <= len(s):
                sub_str = s[j:j+w_size]
                # a valid str
                if ctr[sub_str]:
                    tmp_ctr[sub_str] += 1
                    if tmp_ctr[sub_str] <= ctr[sub_str]:
                        count += 1
                    else:
                        while tmp_ctr[sub_str] > ctr[sub_str]:
                            str1 = s[left:left+w_size]
                            tmp_ctr[str1] -= 1
                            if tmp_ctr[str1] < ctr[str1]:
                                count -= 1
                            left += w_size
                    # a valid result
                    if count == len(words):
                        res.append(left)
                        count -= 1
                        tmp_ctr[s[left:left+w_size]] -= 1
                        left += w_size
                else:  # not valid word, reset
                    tmp_ctr = Counter()
                    count = 0
                    left = j + w_size
                j += w_size

        return res


# Too slow
# from collections import Counter
# class Solution(object):
#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """
#         # note that words may contain duplicate words
#         if not s or not words:
#             return []
        
#         w_size = len(words[0])
#         total_size = len(words) * w_size
#         if len(s) < total_size:
#             return []

#         res = []
#         for i in range(len(s)-total_size+1):
#             # determine substring starting with i is valid
#             j = i
#             ctr = Counter(words)
#             valid = True
#             while j < i+total_size:
#                 w = s[j:j+w_size]
#                 if w in ctr and ctr[w] > 0:
#                     ctr[w] -= 1
#                 else:
#                     valid = False
#                     break
#                 j += w_size
#             if valid:
#                 res.append(i)
#         return res




class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    # self.assertEqual(self.s.method(), None)
    # s = 'barfoothefoobarman'
    # words = ['foo', 'bar']
    # self.assertEqual(self.s.findSubstring(s, words), [0,9])

    # s = 'barfoobarthefoobarman'
    # words = ['foo', 'bar', 'bar']
    # self.assertEqual(self.s.findSubstring(s, words), [0])

    # s = 'barfoofoobarthefoobarman'
    # words = ["bar","foo","the"]
    # self.assertEqual(self.s.findSubstring(s, words), [6,9,12])

    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    self.assertEqual(self.s.findSubstring(s, words), [8])

if __name__ == "__main__":
  unittest.main()
