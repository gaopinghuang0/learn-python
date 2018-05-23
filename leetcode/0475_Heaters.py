
# beats 83.40%
import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # idea: for each house, find nearest heater using bisect
        heaters.sort()
        res = 0
        n = len(heaters)
        for house in houses:
            pos = bisect.bisect_left(heaters, house)
            if pos == 0:
                min_dist = abs(house - heaters[pos])
            elif pos == n:
                min_dist = abs(house - heaters[pos-1])
            else:
                dist1 = abs(house - heaters[pos-1])
                dist2 = abs(house - heaters[pos])
                min_dist = min(dist1, dist2)
            if res < min_dist:
                res = min_dist
        return res


class Solution_Too_Slow(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # idea: increase radius one by one
        house_dict = {house:True for house in houses}
        for h in heaters:
            if h in house_dict:
                del house_dict[h]
        radius = 0
        while house_dict:
            radius += 1
            for h in heaters:
                x = h-radius
                if x in house_dict:
                    del house_dict[x]
                x = h+radius
                if x in house_dict:
                    del house_dict[x]
        return radius



sol = Solution()
print(sol.findRadius([2], [2]))  # 0
print(sol.findRadius([1,2,3], [2]))  # 1
print(sol.findRadius([1,2,3,4], [1,4]))  # 1
print(sol.findRadius([1,2,3,4], [1]))  # 3
houses = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
heaters = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
print(sol.findRadius(houses, heaters))  # 161834419