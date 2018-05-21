# calculate 1+2+3+...+n
# cannot use times, division, for, while, switch, case, if, else, A?B:C
#《剑指offer》第46题

def special_sum(n):
    return n and n+special_sum(n-1)

print(special_sum(10))
print(special_sum(100))