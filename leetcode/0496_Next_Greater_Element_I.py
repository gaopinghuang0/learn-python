
# O(n) idea from Discuss, beats 57.18%
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # We use a stack to keep a decreasing sub-sequence, whenever we see a number x greater than stack.peek() we pop all elements less than x and for all the popped ones, their next greater element is x
        # For example [9, 8, 7, 3, 2, 1, 6]
        # The stack will first contain [9, 8, 7, 3, 2, 1] and then we see 6 which is greater than 1 so we pop 1 2 3 whose next greater element should be 6
        cache, stack = {}, []
        for n in nums:
            while len(stack) and stack[-1] < n:
                cache[stack.pop()] = n
            stack.append(n)

        return [cache.get(n, -1) for n in findNums]
        