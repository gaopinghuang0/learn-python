
# beats 8.11%
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1], [1,1]]
        for _ in range(numRows-2):
            temp = [1]
            prev = res[-1]
            mid = len(prev) // 2
            # print(len(prev), mid)
            for i in range(mid):
                temp.append(prev[i]+prev[i+1])
            if len(prev) % 2 == 1:
                temp = temp + temp[::-1]
            else:
                temp = temp + temp[:-1][::-1]
            res.append(temp)
        return res

obj = Solution()
print(obj.generate(5))
print(obj.generate(6))
