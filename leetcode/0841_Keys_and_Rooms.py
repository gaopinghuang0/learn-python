import unittest

# beats 100%
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # idea: use two sets to maintain visited and to-be-visited
        visited = {0}
        n = len(rooms)
        todo = set(rooms[0])
        while todo:
            i = todo.pop()
            if i not in visited:
                visited.add(i)
                for j in rooms[i]:
                    if j not in visited:
                        todo.add(j)

        return len(visited) == n


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.canVisitAllRooms([[1],[2],[3],[]]), True)
        self.assertEqual(self.s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]), False)


if __name__ == "__main__":
    unittest.main()
