# packing_melons.py

def melon_count(boxes, melons):
	b = len(boxes)
	m = len(melons)
	dp = [[0]*b]*m
	i = 0
	while i < m:
		j = 0
		put = False
		while j < b:
			if melons[i] > boxes[j]:
				dp[i][j] = dp[i][j-1]
			else:
				dp[i][j] = dp[i-1][j-1] + 1
				while j < b-1:
					dp[i][j+1] = dp[i][j]
					j += 1
			j += 1
		i += 1
	# print dp
	return dp[m-1][b-1]

# def melon_count(boxes, melons):
# 	m, b = len(melons), len(boxes)
# 	res = {}
# 	for start in xrange(m):
# 		i, j = start, 0
# 		res[start] = 0
# 		while i < m:
# 			while j < b:
# 				if melons[i] <= boxes[j]:
# 					res[start] += 1
# 					j += 1
# 					break
# 				j += 1
# 			i += 1
# 	return max(res.values())

print melon_count([3,4,5, 6], [1,2])
print melon_count([3,7,9,1,2,8], [8,1,2,5])


arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
# print sum(map(lambda x: (x[0]-x[1])**2, zip(arr1, arr2)))


