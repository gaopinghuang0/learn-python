# idea optimized based on top submission, beats 99.53%
import collections, itertools, math
class Solution(object):
    def minAreaFreeRect(self, points):
        points = [complex(*z) for z in sorted(points)]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            seen[Q - P].append((P + Q) / 2)

        min_area_square = float("inf")
        for A, candidates in seen.iteritems():
            for P, Q in itertools.combinations(candidates, 2):
                D = P - Q
                if A.real * D.real == -A.imag * D.imag:
                    area_square = (A.real**2 + A.imag**2) * (D.real**2 + D.imag**2)
                    if area_square < min_area_square:
                        min_area_square = area_square
        return math.sqrt(min_area_square) if min_area_square != float("inf") else 0

# # idea 1, beats 40.76%
# import collections, math
# class Solution(object):
#     def minAreaFreeRect(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: float
#         """
#         # idea: compute slope for every two points
#         def get_slope(p1, p2):
#             "Return string instead of float to make the slope more accurate"
#             x1, y1 = p1
#             x2, y2 = p2
#             if x1 == x2:
#                 return 'inf'
#             if y1 == y2:
#                 return '0'
#             slope = float(y2 - y1) / (x2 - x1)
#             return str(slope)[:7]

#         def get_area_square(pair1, pair2):
#             "Return None if not a rect"
#             p1, p2 = pair1
#             p3, p4 = pair2

#             x1, y1 = points[p1]
#             x2, y2 = points[p2]
#             x3, y3 = points[p3]
#             x4, y4 = points[p4]
#             # v12 = (x2-x1, y2-y1)
#             # v13 = (x3-x1, y3-y1)
#             # dot product
#             if (x2-x1) * (x3-x1) + (y2-y1) * (y3-y1) == 0:
#                 if (x2-x1) * (x4-x2) + (y2-y1) * (y4-y2) == 0:
#                     # form a rect
#                     area_square = ((x2-x1)**2 + (y2-y1)**2) * ((x3-x1)**2 + (y3-y1)**2)
#                     return area_square
#                 return None
#             # v14 = (x4-x1, y4-y1)
#             if (x2-x1) * (x4-x1) + (y2-y1) * (y4-y1) == 0:
#                 if (x2-x1) * (x3-x2) + (y2-y1) * (y3-y2) == 0:
#                     # form a rect
#                     area_square = ((x2-x1)**2 + (y2-y1)**2) * ((x4-x1)**2 + (y4-y1)**2)
#                     return area_square
#             return None

#         slopes = collections.defaultdict(list)
#         n = len(points)
#         for i in xrange(n-1):
#             for j in xrange(i+1, n):
#                 slope = get_slope(points[i], points[j])
#                 slopes[slope].append((i, j))
        
#         min_area_square = float('inf')
#         for slope, pairs in slopes.items():
#             if len(pairs) < 2:
#                 continue
#             # try each pair
#             m = len(pairs)
#             for i in xrange(m):
#                 for j in xrange(m):
#                     if i != j:
#                         area_square = get_area_square(pairs[i], pairs[j])
#                         if area_square is None:
#                             continue
#                         if area_square < min_area_square:
#                             min_area_square = area_square
        
#         return math.sqrt(min_area_square) if min_area_square != float('inf') else 0