

# beats 93.97%
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def parse(s):
            n = len(s)
            x, b = [], []
            i = 0
            start = 0
            while i <= n:
                if i == n or s[i] in ['+', '-']:
                    temp = s[start:i]
                    if temp.endswith('x'):
                        x.append(temp)
                    else:
                        b.append(temp)
                    start = i
                i += 1
            # replace x by 1 or remove x
            newx = []
            for elem in x:
                if len(elem) > 1 and '0' <= elem[-2] <= '9':
                    newx.append(elem[:-1])
                else:
                    newx.append(elem[:-1]+'1')
            # print(newx, b)
            return sum(int(i) if i else 0 for i in newx), sum(int(i) if i else 0 for i in b)


        left, right = equation.split('=')
        left, right = parse(left), parse(right)
        # print(left, right)
        if left == right:
            return 'Infinite solutions'
        elif left[0] == right[0] and left[1] != right[1]:
            return 'No solution'
        else:
            return 'x='+str((right[1]-left[1])//(left[0]-right[0]))


sol = Solution()
print(sol.solveEquation("x+5-3+x=6+x-2"))  # x=2
print(sol.solveEquation("x=x"))  # Infinite solutions
print(sol.solveEquation("2x=x"))  # x=0
print(sol.solveEquation("2x+3x-6x=x+2"))  # x=-1
print(sol.solveEquation("x=x+2"))  # No solution
print(sol.solveEquation("-x=-1"))  # x=1
