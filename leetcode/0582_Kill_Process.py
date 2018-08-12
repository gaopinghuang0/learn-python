import unittest

# optimize, beats 90.82%
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        # idea: use a dict
        parent_to_childen = {}  # {ppid: set(pid,)}
        for x, y in zip(pid, ppid):
            if y in parent_to_childen:
                parent_to_childen[y].append(x)
            else:
                parent_to_childen[y] = [x]
        stack = [kill]
        res = []
        while stack:
            ppid = stack.pop()
            res.append(ppid)
            if ppid in parent_to_childen:  # is a ppid
                stack += parent_to_childen[ppid]
        return res

# beats 1.53%
class Solution_V1(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        # idea: use a dict
        parent_to_childen = {}  # {ppid: set(pid,)}
        for x, y in zip(pid, ppid):
            if y in parent_to_childen:
                parent_to_childen[y].add(x)
            else:
                parent_to_childen[y] = set([x])
        stack = [kill]
        res = set([kill])
        while stack:
            ppid = stack.pop()
            if ppid in parent_to_childen:  # is a ppid
                res = res.union(parent_to_childen[ppid])
                stack += list(parent_to_childen[ppid])
            else:  # just a pid, no child process
                res.add(ppid)
        return list(res)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        pid =  [1, 3, 10, 5]
        ppid = [3, 0, 5, 3]
        kill = 5
        self.assertEqual(self.s.killProcess(pid, ppid, kill), [5,10])


if __name__ == "__main__":
    unittest.main()
