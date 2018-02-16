import unittest

# idea from Discuss, beats 24.81%
import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # idea: dfs, but a node could be visited for multiple times
        # Below is the idea:
        # The following is my summary. Hope it will help others:
        # some observations:
        # The nodes which have odd degrees (int and out) are the entrance or exit. In your example it’s JFK and A.
        # If there are no nodes have odd degrees, we could follow any path without stuck until hit the last exit node
        # The reason we got stuck is because that we hit the exit
        # In your given example, nodes A is the exit node, we hit it and it’s the exit. So we put it to the result as the last node.
        # credit: https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C++

        targets = collections.defaultdict(list)
        for t in sorted(tickets, reverse=True):
            targets[t[0]].append(t[1])
        stack = ['JFK']
        path = []
        while stack:
            while targets[stack[-1]]:
                stack.append(targets[stack[-1]].pop())
            path.append(stack.pop())
        return path[::-1]


class SolutionWrong(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # idea: use a dict, for each "FROM", store a sorted list of "TO"
        if not tickets:
            return []
        lookup = defaultdict(list)
        for t in tickets:
            lookup[t[0]].append(t[1])
        for key in lookup:
            lookup[key].sort(reverse=True)
        # print(lookup)
        _from = 'JFK'
        res = [_from]
        while lookup:
            # print(_from, lookup)
            all_to = lookup[_from]
            if not all_to:
                break
            for i in range(len(all_to)-1, -1, -1):
                to = all_to[i]
                if to in lookup:
                    break
            res.append(to)
            if to in lookup:
                all_to.pop(i)
                if not all_to:
                    del lookup[_from]
            _from = to
        return res

class TestSolution(unittest.TestCase):
  def setUp(self):
    self.s = Solution()

  def test_method(self):
    """Such as self.assertEqual, self.assertTrue"""
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    self.assertEqual(self.s.findItinerary(tickets), ["JFK", "MUC", "LHR", "SFO", "SJC"])
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    self.assertEqual(self.s.findItinerary(tickets), ["JFK","ATL","JFK","SFO","ATL","SFO"])
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    self.assertEqual(self.s.findItinerary(tickets), ["JFK",'NRT','JFK','KUL'])

if __name__ == "__main__":
  unittest.main()
