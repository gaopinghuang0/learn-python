import unittest


class Solution(object):
    # sample Solution using DP
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        Idea: store seen char. If there is seen char (i.e., repeat)
            between curr_start and curr char, then we can
            directly jump to seen char and use as new current_start
            because starting with any char before seen char cannot have a longer substring.
        """
        seen = {}
        curr_start = 0
        curr_len = 0
        max_len = 0
        for i, ch in enumerate(s):
            if ch in seen and seen[ch] >= curr_start:
                curr_start = seen[ch] + 1
                curr_len = i - seen[ch]
                seen[ch] = i
            else:
                seen[ch] = i
                curr_len = i - curr_start + 1
                if max_len < curr_len:
                    max_len = curr_len
        return max_len

    # # ok, but slow
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """

    #     """
    #     Idea: binary search
    #         check lower, upper and middle, update lower and upper
    #     """
    #     def isValidSubstring(length):
    #         for i in range(n-length+1):
    #             if len(set(s[i:i+length])) == length:
    #                 return True
    #         return False

    #     n = len(s)
    #     m = len(set(s))
    #     if m == n:
    #         return n
    #     if m < 2:
    #         return m

    #     lower = 1
    #     upper = m
    #     if isValidSubstring(upper):
    #         return upper
    #     while lower < upper:
    #         mid = (lower + upper) // 2
    #         if mid == lower:
    #             break
    #         if isValidSubstring(mid):
    #             lower = mid
    #         else:
    #             upper = mid
    #     return lower





    # wrong
    # def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """    
        # def _lengthOfLongestSubstring(s):
        #     global g_res

        #     n = len(s)
        #     m = len(set(s))
        #     if m == n:
        #         return n
        #     if m < 2:
        #         return m

        #     left = _lengthOfLongestSubstring(s[:n//2])
        #     right = _lengthOfLongestSubstring(s[n//2:])
        #     res = max(left, right)   # check if the whole string has a substring longer than res 

        #     print(g_res, res)
        #     if g_res >= res:
        #         return g_res

        #     if res >= n:
        #         g_res = max(g_res, res)
        #         return res

        #     while 1:
        #         temp = res + 1
        #         found = False
        #         for i in range(n-temp+1):
        #             if len(set(s[i:i+temp])) == temp:
        #                 found = True
        #         print(temp, s, found, g_res)
        #         if found:
        #             res += 1
        #         else:
        #             break

        #     g_res = max(g_res, res)
        #     return res
        
        # # Since g_res is defined in the scope of self.lengthOfLongestSubstring,
        # # it's local and not the same as the nested global g_res in _lengthOfLongestSubstring.
        # # We need to mark it as global as well.
        # global g_res
        # g_res = 0
        # return _lengthOfLongestSubstring(s)




    # Abanton: too slow
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     n = len(s)
    #     if n < 2:
    #       return n

    #     res = 0
    #     for i in range(n-1):
    #       cache = {}
    #       cache[s[i]] = None

    #       # stop search if res is larger than the remaining chars
    #       if res >= (n-i):
    #           break
    #       for j in range(i+1, n):
    #           if s[j] not in cache:
    #               cache[s[j]] = None
    #               res = max(res, j-i+1)
    #           else:
    #               res = max(res, j-i)
    #               break
    #     return res



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual(self.s.lengthOfLongestSubstring('bbbbb'), 1)
        self.assertEqual(self.s.lengthOfLongestSubstring('abcd'), 4)
        self.assertEqual(self.s.lengthOfLongestSubstring(''), 0)
        self.assertEqual(self.s.lengthOfLongestSubstring('b'), 1)
        self.assertEqual(self.s.lengthOfLongestSubstring('pwwkew'), 3)
        self.assertEqual(self.s.lengthOfLongestSubstring('abcdbcbb'), 4)
        self.assertEqual(self.s.lengthOfLongestSubstring('abcccade'), 4)
        self.assertEqual(self.s.lengthOfLongestSubstring('aabbcc'), 2)
        self.assertEqual(self.s.lengthOfLongestSubstring('dvdf'), 3)
        self.assertEqual(self.s.lengthOfLongestSubstring('jlygy'), 4)


if __name__ == "__main__":
    unittest.main()
