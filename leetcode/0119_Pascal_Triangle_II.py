
# beats 69.63%
class Solution(object):
    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[1]
        for i in range(1,numRows+1):
            item=[1]
            for j in range(1,i):
                item.append(res[j-1]+res[j])
            item.append(1)
            res = item
        return res

obj = Solution()
print(obj.getRow(5))
print(obj.getRow(6))
