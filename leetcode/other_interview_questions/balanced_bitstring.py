"""
Balanced BitString
Code Forces 1405: https://codeforces.com/contest/1405/problem/C
Solution inspired by: https://zhuanlan.zhihu.com/p/262869343

Description:
给定一个字符串，字符串当中只包含三种字符，分别是0，1和?。 ?表示既可以是0也可以是1。
现在呢，给定一个整数k，k表示滑动窗口的长度。我们需要从头开始将一个滑动窗口向字符串末尾移动，
很明显，不管我们怎么移动，滑动窗口里的字符的数量应该都是k个。

由于存在?既可以是0也可以是1，我们希望我们能找到一种方案，
把一部分？变成0，另外一部分变成1。使得在这个窗口滑动的过程当中，
窗口里的0的数量和1的数量相等。

给定字符串以及k，要求返回YES或NO，YES表示存在这样的方案，NO表示不存在。

Example:
见测试用例
"""

def check_balanced_bitstring(n, k, s):
    """
    Idea: s[i] must be equal to s[i+k], s[i+2k], ...
    Use an array with length k to store known bits.
    """
    if k % 2 == 1:
        return 'NO'

    dp = [None] * k
    for i, ch in enumerate(s):
        idx = i % k
        bit = dp[idx]
        if ch == '?':
            continue
        if bit is not None and bit != ch:
            return 'NO'
        dp[idx] = ch
    
    # count the total number of 1s and 0s
    one, zero = 0, 0
    for num in dp:
        if num == '0':
            zero += 1
        elif num == '1':
            one += 1
        
    if max(one, zero) > k // 2:  # Known bits are more than half
        return 'NO'

    return 'YES'

assert check_balanced_bitstring(6, 4, '100110') == 'YES'
assert check_balanced_bitstring(3, 2, '1?1') == 'YES'
assert check_balanced_bitstring(3, 2, '1?0') == 'NO'
assert check_balanced_bitstring(4, 4, '????') == 'YES'
assert check_balanced_bitstring(7, 4, '1?0??1?') == 'YES'
assert check_balanced_bitstring(10, 10, '11??11??11') == 'NO'
assert check_balanced_bitstring(4, 2, '1??1') == 'NO'
assert check_balanced_bitstring(4, 4, '?0?0') == 'YES'
assert check_balanced_bitstring(6, 2, '????00') == 'NO'
print("All passed")