# find all articulation points or cut vertices
# https://leetcode.com/discuss/interview-question/436073/

import unittest

from typing import List
from collections import defaultdict

# idea: Tarjan's algorithm
class Solution:
    def find_all_cut_vertices(self, numNodes: int, numEdges: int, edges: List[List[int]]) -> List[int]:
        desc = [-1] * numNodes
        low = [numNodes+1] * numNodes
        res = set()
        self.time = 1

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u, parent):
            desc[u] = low[u] = self.time
            self.time += 1
            child = 0
            for v in graph[u]:
                if desc[v] == -1: # not visited
                    dfs(v, u)
                    child += 1
                    low[u] = min(low[u], low[v])

                    if parent is None and child > 1:  # case 1
                        res.add(u)
                    
                    if parent is not None and low[v] >= desc[u]:  # case 2
                        res.add(u)

                elif parent != v:
                    low[u] = min(low[u], desc[v])


        for node in range(numNodes):
            if desc[node] == -1:  # not visited
                dfs(node, None)

        return sorted(res)

# Other's solution. I feel it is wrong.
# https://leetcode.com/problems/critical-connections-in-a-network/discuss/808304/Python-dfs-(personally-easiest-to-understand)
# Use the second test case, I confirm this solution is wrong.
class Solution2(object):
    def find_all_cut_vertices(self, n, _, edges):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
            
        dfn = [None]*n
        low = [None]*n
        out = []
        self.depth = 0
        def dfs(u,parent):                
            dfn[u] = low[u] = self.depth
            self.depth+=1
            for v in g[u]:
                if dfn[v] == None:
                    dfs(v,u)
                    if dfn[u] < low[v]: 
                        '''
                        low[x] = essentially a strongly connected network defined by the earliest node...
                        
                        
                        dfn[u] < low[v]
                        if depth of recursion of u is earlier than the "network of v defined by the earliest node,"
                        then its guaranteed that v is not reachable without the existing connection.
                        
                        dfn[u] >= low[v]
                        if depth of recursion of u is later than or equal to the "network of v defined by the earliest node,"
                        we know that u comes later than the network, so it is reachable
                        ''' 
                        out.append(u)

                if v!=parent: # one full loop means that there is a low point that wasn't the parent
                    low[u] = min(low[u],low[v])
        dfs(0,None)
        return sorted(out)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.s2 = Solution2()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        numNodes = 7
        numEdges = 7
        edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
        self.assertEqual(self.s.find_all_cut_vertices(numNodes, numEdges, edges), [2, 3, 5])
        self.assertEqual(self.s2.find_all_cut_vertices(numNodes, numEdges, edges), [2, 3, 5])

        numNodes = 7
        numEdges = 8
        edges = [[0, 1], [1, 2], [2, 3], [3, 0], [2, 4], [4,5], [5, 2], [3,6]]
        self.assertEqual(self.s.find_all_cut_vertices(numNodes, numEdges, edges), [2, 3])
        self.assertEqual(self.s2.find_all_cut_vertices(numNodes, numEdges, edges), [2, 3])


if __name__ == "__main__":
    unittest.main()
