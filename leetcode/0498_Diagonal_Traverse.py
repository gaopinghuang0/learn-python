
# beats 25.25%
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        i, j = 0, 0
        is_up_right = True
        m, n = len(matrix), len(matrix[0])
        res = []
        while not (i == m-1 and j == n-1):
            res.append(matrix[i][j])
            if is_up_right:
                if j == n-1:  # reach right border
                    i += 1
                    is_up_right = False
                elif i == 0:
                    j += 1
                    is_up_right = False
                else:   # in the middle
                    i -= 1
                    j += 1
            else:
                if i == m-1:  # reach bottom border
                    j += 1
                    is_up_right = True
                elif j == 0:
                    i += 1
                    is_up_right = True
                else:
                    i += 1
                    j -= 1
        res.append(matrix[i][j])
        return res


obj = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(obj.findDiagonalOrder(matrix))
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
 [ 10, 11, 12]
]
print(obj.findDiagonalOrder(matrix))
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ],
 [ 10, 11, 12],
 [ 13, 14, 15]
]
print(obj.findDiagonalOrder(matrix))
matrix = [
 [ 1, 2, 3 ]
]
print(obj.findDiagonalOrder(matrix))
matrix = [
 [ 1 ],
 [ 4 ],
 [ 7 ],
 [ 10 ]
]
print(obj.findDiagonalOrder(matrix))