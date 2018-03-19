
# beats 61.27%
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # idea: from right to left and find the first decreasing sequence
        int_max = 2**31 - 1
        s = list(str(n))
        stack = []
        for i in range(len(s))[::-1]:
            x = s[i]
            if not stack or x >= stack[-1][0]:
                stack.append((x,i))
            else:
                prev = stack.pop()
                while stack and x < stack[-1][0]:
                    prev = stack.pop()
                if prev[0] > x:
                    s[i], s[prev[1]] = prev[0], x
                    s[i+1:] = s[i+1:][::-1]  # reverse
                    if int(''.join(s)) > int_max:
                        return -1
                    else:
                        return int(''.join(s))
        return -1

obj = Solution()
print(obj.nextGreaterElement(12))
print(obj.nextGreaterElement(21))
# print(obj.nextGreaterElement(2**31-104))
print(obj.nextGreaterElement(230241))



