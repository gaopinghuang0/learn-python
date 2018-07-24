import unittest


"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

# beats 18.59%
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # idea: first build a map of id to index, then use a stack like a dfs
        lookup = {}  # {id: employee}
        for employee in employees:
            lookup[employee.id] = employee

        # build a dependency of nodes in the stack
        stack = [id]
        subordinates = lookup[id].subordinates
        while subordinates:
            stack += subordinates
            next_level = []
            for id in subordinates:
                next_level += lookup[id].subordinates
            subordinates = next_level

        while stack:
            id = stack.pop()
            subordinates = lookup[id].subordinates
            if subordinates:
                lookup[id].importance += sum(lookup[_id].importance for _id in subordinates)
        return lookup[id].importance




class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.method(), None)


if __name__ == "__main__":
    unittest.main()
