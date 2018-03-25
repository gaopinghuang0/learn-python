
# beats 95.86%
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # idea: use a dict to store idx,value
        lookup = {}
        for i, v in enumerate(list1):
            lookup[v] = i
        res = []
        min_sum = float('inf')
        for j, y in enumerate(list2):
            if y in lookup:
                new_sum = lookup[y] + j
                if new_sum < min_sum:
                    min_sum = new_sum
                    res = [y]
                elif new_sum == min_sum:
                    res.append(y)
                else:
                    pass
        return res

obj = Solution()
A = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
B = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
print(obj.findRestaurant(A, B))
A = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
B = ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
print(obj.findRestaurant(A, B))

A = ["Shogun", "KFC", "Tapioca Express", "Burger King"]
B = ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun", "KFC"]
print(obj.findRestaurant(A, B))
