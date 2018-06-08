
# idea from Discuss, beats 29.18%
# https://leetcode.com/problems/redundant-connection/discuss/107984/10-line-Java-solution-Union-Find.
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # idea from Discuss, disjoint set
        # note that # of nodes will be smaller than 1000
        parent = list(range(1001))  # set node's parent to itself
        def find(f):  # find the root of this node
            if f != parent[f]:
                parent[f] = find(parent[f])  # update node and its parents to point to root directly
            return parent[f]
        for s, e in edges:
            find_s = find(s)
            find_e = find(e)
            if find_s == find_e:  # if two nodes has same root, return
                return [s, e]
            else:
                parent[find_s] = find_e
        return []


from collections import defaultdict
import time
class Solution_Wrong(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # idea: DFS, return the edge that causes a cycle
        # build graph
        graph = defaultdict(list)   # {node: [neighbors]}
        for edge in edges:
            s, e = edge
            graph[s].append(e)
            graph[e].append(s)
        print(graph)
        # dfs using stack, find a cycle
        visited = set()
        stack = [1]
        parent = {}  # {node: parent}
        prev = None
        while stack:
            node = stack.pop()
            print(node, stack)
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                parent[node] = prev
                prev = node
                print(visited, stack, prev)
            else:
                break
        print(prev, parent)
        # the edge to form a cycle is prev -> node
        # find all edges in the cycle
        cycle_edges = set()
        while prev != node:
            if prev > node:
                cycle_edges.add((node, prev))
            else:
                cycle_edges.add((prev, node))
            prev = parent[prev]
        # find the edge that is in the cycle from right to left
        for edge in edges[::-1]:
            if tuple(edge) in cycle_edges:
                return edge


sol = Solution()
print(sol.findRedundantConnection([[1,2], [1,3], [2,3]]))  # [2,3]
print(sol.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))  # [1,4]
# print(sol.findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]]))  # [1,3]
