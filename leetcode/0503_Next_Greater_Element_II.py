
# beats 38.42%
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # idea: use two stacks, one to store decreasing, one to store increasing
        if not nums:
            return []
        dec_stack, inc_stack = [], [nums[0]]
        res = [-1]*len(nums)
        for i, x in enumerate(nums):
            while len(dec_stack) and dec_stack[-1][0] < x:
                res[dec_stack.pop()[1]] = x
            dec_stack.append((x, i))
            if x > inc_stack[-1]:
                inc_stack.append(x)

        # need to search circularly
        # print(dec_stack, inc_stack)
        # now it's the same as 0496_NextGreaterElements_I
        cache = {}
        prev = inc_stack[0]
        for x in inc_stack[1:]:
            cache[prev] = x
            prev = x

        for x, i in dec_stack:
            if x in cache:
                res[i] = cache[x]
            else:
                for y in inc_stack:
                    if x < y:
                        res[i] = y
                        break
        return res

class SolutionOld(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # idea: use a stack to store decreasing, a cache to store increasing
        if not nums:
            return []
        dec_stack, cache = [], {}
        prev = nums[0]
        res = [-1]*len(nums)
        for i, x in enumerate(nums):
            while len(dec_stack) and dec_stack[-1][0] < x:
                res[dec_stack.pop()[1]] = x
            dec_stack.append((x, i))
            if x > prev:
                cache[prev] = x
                prev = x

        # need to search circularly
        # print(dec_stack, cache)
        # now it's the same as 0496_NextGreaterElements_I
        for x, i in dec_stack:
            res[i] = cache.get(x, -1)

        return res

obj = Solution()
print(obj.nextGreaterElements([1,2,1]))
print(obj.nextGreaterElements([5,4,3,2,1]))
