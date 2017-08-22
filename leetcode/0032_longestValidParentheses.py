class Solution(object):
	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		# Time limit exceeded
		# def is_valid(s):
		# 	while True:
		# 		if '()' in s:
		# 			s = s.replace('()', '')
		# 		else:
		# 			break
		# 	return not s
		# res = 0
		# i = 0
		# j = 0
		# changed = 0
		# size = len(s)
		# while i < size:
		# 	j = i+1
		# 	while j <= size:
		# 		if is_valid(s[i:j]) and (j-i) > res:
		# 			res = j - i
		# 			changed = j
		# 			j += 2
		# 		else:
		# 			j += 1
		# 	print i, j, changed
		# 	if changed:
		# 		i = changed
		# 	else:
		# 		i += 1
		# 	changed = 0
		# return res

		# DP Solution
		# Credit: https://discuss.leetcode.com/topic/52921/5-liner-in-python-dp-84ms
		dp = [0] * len(s)
		maxL = 0
		for i in range(1, len(s)):
			if s[i] == ')':
				j = i - 1 - dp[i-1]    # eg., ((()))
				if j >= 0 and s[j] == '(':
					dp[i] = dp[i-1] + 2
					if j - 1 >= 0:
						dp[i] += dp[j-1]  # eg., ()((()))
					maxL = max(maxL, dp[i])
		return maxL

# print Solution().longestValidParentheses('")))()(()))())(())()())(()((())))())))))(())))(()()))(())())())))(()))()))((((()())))))()()))(()((())((())())()()()()((()((((())))(()))(()()()))))(()((((()))(((((()))())()))((("')
print Solution().longestValidParentheses("))))())()()(()")