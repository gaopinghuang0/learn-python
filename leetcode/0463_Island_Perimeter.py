
# beats 8.48%
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # idea: dfs
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        res = 0
        stack = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    stack.append((i, j))
                    visited[i][j] = 1
                    break
            if stack:
                break
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while stack:
            # print(stack, res)
            i, j = stack.pop()
            for direction in directions:
                x, y = i+direction[0], j+direction[1]
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    if grid[x][y]:  # island
                        stack.append((x,y))
                        visited[x][y] = 1
                    else:
                        res += 1
                elif x < 0 or x >= m or y < 0 or y >= n:
                    res += 1
        return res

sol = Solution()
# print(sol.islandPerimeter([[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]))

print(sol.islandPerimeter([[0],[1]]))
print(sol.islandPerimeter([[1,1],[1,1]]))
