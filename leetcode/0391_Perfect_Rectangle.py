
# idea from Discuss, beats 50.85%
import sys
from collections import defaultdict
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # idea:
        # Save area and all FOUR corners for each sub-rectangle:
        # 1. sum of area of all sub-rectangle == area of maximum rectangle.
        # 2. each corner should only appear either TWO or FOUR times,
        # except four corners of big rectangle.
        if not rectangles or not rectangles[0]:
            return False
        lx, ly, rx, ry = sys.maxsize, sys.maxsize, 0, 0
        area = 0
        corners = defaultdict(int)
        for x1, y1, x2, y2 in rectangles:
            lx, ly, rx, ry = min(lx, x1), min(ly, y1), max(rx, x2), max(ry, y2)
            area += (x2 - x1) * (y2 - y1)
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                corners[corner] += 1
        # print(lx, ly, rx, ry, area)        
        if area != (rx - lx) * (ry - ly):
            return False
        for corner in [(lx, ly), (lx, ry), (rx, ry), (rx, ly)]:
            if corner not in corners or corners[corner] != 1:
                return False
            corners[corner] = 2

        for corner, count in corners.items():
            if count != 2 and count != 4:
                return False
        return True


# time limit exceeded; may also memory limit exceeded
import sys
class Solution_WRONG(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # idea: find the global rectangle as a 2D matrix
        if not rectangles or not rectangles[0]:
            return True
        pos = [sys.maxsize, sys.maxsize, 0, 0]
        for rect in rectangles:
            pos[0] = min(pos[0], rect[0])
            pos[1] = min(pos[1], rect[1])
            pos[2] = max(pos[2], rect[2])
            pos[3] = max(pos[3], rect[3])
        # print(pos)
        # init a 2D matrix
        x0, y0 = pos[:2]  # origin
        w, h = pos[2] - x0, pos[3] - y0
        matrix = [[0]*w for _ in range(h)]
        # cover each rect
        for rect in rectangles:
            for i in range(rect[1]-y0, rect[3]-y0):
                for j in range(rect[0]-x0, rect[2]-x0):
                    if matrix[i][j]:  # overlapping
                        return False
                    matrix[i][j] = 1
        # check every point of matrix is covered
        for i in range(h):
            for j in range(w):
                if not matrix[i][j]:
                    return False
        return True

sol = Solution()
rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
print(sol.isRectangleCover(rectangles))
rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]
print(sol.isRectangleCover(rectangles))
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]
print(sol.isRectangleCover(rectangles))

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]
print(sol.isRectangleCover(rectangles))





