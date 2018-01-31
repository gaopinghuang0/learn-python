
# beats 68.09%
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # idea: build a directed graph from equations
        # use 2D matrix to represent graph
        variables = set()
        for equation in equations:
            for var in equation:
                variables.add(var)
        # print(variables)
        variable_dict = {v:i for i, v in enumerate(variables)}
        # print(variable_dict)
        m = n = len(variables)
        graph = [[0]*m for _ in range(n)]
        for equation, value in zip(equations, values):
            i, j = variable_dict[equation[0]], variable_dict[equation[1]]
            graph[i][j] = value
            graph[j][i] = 1 / value
        # print(graph)
        res = []
        for query in queries:
            x, y = query[0], query[1]
            if x in variable_dict and y in variable_dict:
                if x == y:
                    res.append(1.0)
                else:
                    i, j = variable_dict[x], variable_dict[y]
                    seen = set()
                    path = self.find_path(i, j, graph, seen)
                    if path:
                        val = 1.0
                        for i,j in path:
                            val *= graph[i][j]
                        res.append(val)
                    else:
                        res.append(-1.0)
            else:
                res.append(-1.0)
        return res

    def find_path(self, source, target, graph, seen):
        # dfs
        seen.add(source)
        for j, cell in enumerate(graph[source]):
            if cell and j == target:
                return [[source, target]]
            elif cell and j not in seen:
                path = self.find_path(j, target, graph, seen)
                if path:
                    return [[source, j]] + path
        return None

sol = Solution()
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
res = sol.calcEquation(equations, values, queries)
print(res)