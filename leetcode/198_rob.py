import unittest


class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		if len(nums) <= 2:
			return max(nums)

		# dynamic programming
		dp = [nums[0], max(nums[0], nums[1])]
		for i in range(2, len(nums)):
			max_num = nums[i] + dp[-2]
			if max_num > dp[-1]:
				dp.append(max_num)
			else:
				dp.append(dp[-1])
		return dp[-1]

	def rob_not_DP(self, nums):
		"""Use interative way."""
		include, exclude = 0, 0
		for num in nums:
			include, exclude = (exclude+num, max(include, exclude))
		return max(include, exclude)



class TestMethods(unittest.TestCase):
	def setUp(self):
		self.s = Solution()

	def test_method(self):
		data = [2, 1, 1, 3, 4, 4, 9]
		self.assertEqual(self.s.rob(data), self.s.rob_not_DP(data))
		data = [2, 1, 1, 2]
		self.assertEqual(self.s.rob(data), self.s.rob_not_DP(data))


if __name__ == "__main__":
	unittest.main()
