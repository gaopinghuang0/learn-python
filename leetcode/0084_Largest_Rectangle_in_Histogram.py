import unittest

# idea from Discuss, beats 16.08%
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # idea from Discuss, using a stack
        # note: the basic idea is very similar to the Solution_V1 below
        # i.e., try to find the 'left index' and 'right index' efficiently
        # so that the width is (r-l-1), the difference is that we are using a stack
        # to store all the indices.

        # For any bar i, if the bar is higher than the bar at the stack top, push i to stack.
        # If it's lower, then keep poping stack until reach smaller bar. For each removed bar
        # from the stack, say heights[tp], calculate the area of rect with heights[tp] as the
        # smallest bar, the 'left index' is previous item in stack and 'right index'
        # is 'i' (currect index)
        stack = []
        res = 0
        n = len(heights)
        for i, h in enumerate(heights):
            if not stack or h >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and h < heights[stack[-1]]:
                    top = stack.pop()
                    left = stack[-1] if stack else -1
                    res = max(res, heights[top] * (i - left - 1))
                stack.append(i)
        # some elements remaining, now repeat the same process as above
        while stack:
            top = stack.pop()
            left = stack[-1] if stack else -1
            res = max(res, heights[top] * (n - left - 1))
        return res


# idea from Discuss, beats 56.97%
class Solution_V1(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # idea from Discuss
        # for any bar i, the maximum rect is of width r-l-1 where r is the last 
        # bar to the right with height h[r] >= h[i] and l is the last bar to the left
        # with height h[l] >= h[i]
        # the main trick is to find lessFromRight and lessFromLeft efficiently
        if not heights:
            return 0
        n = len(heights)
        lessFromRight = [0]*n
        lessFromLeft = [0]*n
        lessFromLeft[0] = -1
        lessFromRight[-1] = n

        for i in range(1, n):
            p = i-1
            while p >= 0 and heights[p] >= heights[i]:
                p = lessFromLeft[p]
            lessFromLeft[i] = p

        for i in range(n-2, -1, -1):
            p = i+1
            while p < n and heights[p] >= heights[i]:
                p = lessFromRight[p]
            lessFromRight[i] = p

        res = 0
        for i in range(n):
            res = max(res, heights[i] * (lessFromRight[i]-lessFromLeft[i]-1))
        return res


class SolutionTooSlow(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # idea: use a stack to store all consecutive sequence before i-th element
        # each element in the stack is (height, consecutive_width)
        # if the i-th is larger than prev height, increase the width by 1
        # if the i-th is smaller than prev height, decrease the height to the curr height
        stack = []
        res = 0
        for j, curr in enumerate(heights):
            i = 0
            while i < len(stack):
                if stack[i][0] < curr:
                    stack[i][1] += 1
                    res = max(stack[i][0]*stack[i][1], res)
                    i += 1
                elif stack[i][0] == curr:
                    stack[i][1] += 1
                    res = max(stack[i][0]*stack[i][1], res)
                    stack = stack[:i+1]
                    break
                else:
                    stack[i][1] += 1
                    stack[i][0] = curr
                    res = max(curr*stack[i][1], res)
                    stack = stack[:i+1]
                    break
            if not stack or stack[-1][0] != curr:
                stack.append([curr,1])
                res = max(res, curr)
            # print(j, curr, stack,res)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.largestRectangleArea([]), 0)
        self.assertEqual(self.s.largestRectangleArea([2,1,5,6,2,3]), 10)
        self.assertEqual(self.s.largestRectangleArea([999,999,999,999]), 3996)
        self.assertEqual(self.s.largestRectangleArea([3,6,5,7,4,8,1,0]), 20)


if __name__ == "__main__":
    unittest.main()
