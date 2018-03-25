import unittest

# idea from Discuss, beats 66.93%
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea from Discuss, O(n)
        # BFS, each level i are nodes that can be reached in i-1th jump
        n = len(nums)
        if n < 2:
            return 0
        level = 0
        curr_level_end, next_level_end = 0, 0
        i = 0

        while curr_level_end - i + 1 > 0:   # nodes in current level
            level += 1
            while i <= curr_level_end:  # traverse current level and find next level
                next_level_end = max(next_level_end, nums[i]+i)
                if next_level_end >= n-1:  # the last element is in next level
                    return level
                i += 1
            if curr_level_end == next_level_end:  # cannot move to next level
                return float('inf')
            curr_level_end = next_level_end

# Time Limit Exceeded
from heapq import heappush, heappop
class SolutionSlow(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea: min heap from end to start
        if not nums:
            return 0
        n = len(nums)
        hp = [(0,n-1)]
        cache = {}
        cache[n-1] = 0
        for i, v in list(enumerate(nums[:-1]))[::-1]:
            reach = i + v
            print(reach, hp)
            if reach >= n:
                heappush(hp, (1, i))
                cache[i] = 1
            elif v == 0:
                continue
            else:
                temp = []
                while hp:
                    print(temp)
                    if reach >= hp[0][1]:
                        heappush(hp, (hp[0][0]+1, i))
                        cache[i] = hp[0][0]+1
                        while temp:
                            heappush(hp, temp.pop())
                        break
                    else:
                        temp.append(heappop(hp))
                while temp:
                    heappush(hp, temp.pop())
            # print(hp)
        # print(cache)
        return cache[0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.jump([2,3,1,1,4]), 2)
        self.assertEqual(self.s.jump([1,2,0,1]), 2)
        self.assertEqual(self.s.jump([5,9,3,2,1,0,2,3,3,1,0,0]), 3)
        nums = [1,1,1,1,1,1,1]
        self.assertEqual(self.s.jump(nums), 6)



if __name__ == "__main__":
    unittest.main()
