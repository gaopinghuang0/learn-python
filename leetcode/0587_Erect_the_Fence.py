# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

# idea from Discuss, beats 75.00%
# https://leetcode.com/problems/erect-the-fence/discuss/103306/C++-and-Python-easy-wiki-solution
# or check wiki problem: Convex hull algorithms
class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        # idea from Discuss, start from left most nodes, go downside till the right
        # then start over and go upside
        if len(points) <= 1:
            return points
        # sort points
        points = sorted(points, key=lambda p: (p.x, p.y))

        # get cross product of OA and OB vectors
        # return positive if counter-clockwise turn, negative if clockwise, zero if collinear
        def cross(o, a, b):
            return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

        def build(points):
            hull = []
            for p in points:
                while len(hull) >= 2 and cross(hull[-2], hull[-1], p) < 0:
                    hull.pop()
                hull.append(p)
            return hull

        # build lower hull
        lower = build(points)
        # build upper hull
        upper = build(reversed(points))

        # Concatenation of the lower and upper hulls gives the convex hull.
        # Last point of each list is omitted because it is repeated at the
        # beginning of the other list.
        # return lower[:-1] + upper[:-1]
        return list(set(lower[:-1] + upper[:-1]))