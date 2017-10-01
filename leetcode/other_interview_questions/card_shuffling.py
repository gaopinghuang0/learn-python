# https://engineering.purdue.edu/ece264/17au/hw/HW07

def step2(upper, lower):
  """
  Interleave two decks of cards but maintain the relative order within each deck.
  :type upper: List[int]
  :type lower: List[int]
  :rtype list[list[int]]
  """
  # idea: pick the first card from lower deck and insert into every point of upper
  # say insert at upper[i] (i could be [0,len(upper)], from left most to right most)
  # then recursively call function on the right part of upper (upper[i:])
  # and remaining lower (lower[1:])
  m, n = len(upper), len(lower)
  res = []
  if m == 1:
    for i in range(n+1):
      res.append(lower[:i] + upper + lower[i:])
    return res
  if n == 1:
    for i in range(m+1):
      res.append(upper[:i] + lower + upper[i:])
    return res
  first_lower = lower[0]
  # insert first lower inside upper
  for i in range(0, m):
    prefix = upper[:i] + [first_lower]
    for r in step2(upper[i:], lower[1:]):
      res.append(prefix+r)
  # put first lower after upper
  res.append(upper+lower)
  return res

for r in step2([1,2,3], [4,5,6]):
  print(r)

for r in step2([1,2], [4,5]):
  print(r)
