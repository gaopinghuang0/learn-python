
class Solution(object):
  def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """
    # idea: 1D DP
    if not s:
      return 0
    dp = {-1: 1}
    x = s[0]
    if x == '*':
      dp[0] = 9
    elif x == '0':
      return 0
    else:
      dp[0] = 1

    for i, x in enumerate(s[1:], 1):
      n = 0
      prev = s[i-1]
      if x == '0':
        if prev == '1' or prev == '2':
          n += dp[i-2]
        elif prev == '*':
          n += dp[i-2] * 2
        else:
          return 0
      elif x == '*':
        n += dp[i-1] * 9
        if prev == '1':
          n += dp[i-2] * 9
        elif prev == '2':
          n += dp[i-2] * 6
        elif prev == '*':
          n += dp[i-2] * 15
      else:  # '1'-'9'
        n += dp[i-1]
        if prev == '1':
          n += dp[i-2]
        elif prev == '2' and x <= '6':
          n += dp[i-2]
        elif prev == '*' and x <= '6':
          n += dp[i-2] * 2
        elif prev == '*' and x > '6':
          n += dp[i-2]
      dp[i] = n % (10**9 + 7)
    return dp[len(s)-1] % (10**9 + 7)
