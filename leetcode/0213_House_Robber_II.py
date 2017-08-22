import unittest

# Credit: https://discuss.leetcode.com/topic/14375/simple-ac-solution-in-java-in-o-n-with-explanation
class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		size = len(nums)
		if size == 0:
			return 0
		if size <= 2:
			return max(nums)
		# either i-th house is not robbed, break the circle to simpler case
		# or (i+1)-th house not robbed, break the circle
		return max(self.rob_helper(nums[0:size-1]), self.rob_helper(nums[1:size]))

		
	# use the simpler one-row case as helper
	def rob_helper(self, nums):
		include, exclude = 0, 0
		for num in nums:
			include, exclude = (exclude+num, max(include, exclude))
		return max(include, exclude)


class TestSolution(unittest.TestCase):
	def setUp(self):
		self.s = Solution()

	def test_method(self):
		"""Such as self.assertEqual, self.assertTrue"""
		data = []
		self.assertEqual(self.s.rob(data), 0)

		data = [1]
		self.assertEqual(self.s.rob(data), 1)

		data = [2, 1, 1, 2, 3, 4, 5, 6, 7, 1, 9, 6]
		self.assertEqual(self.s.rob(data), 27)


if __name__ == "__main__":
	unittest.main()
