

# beats 5.78%
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target < letters[0]:
            return letters[0]
        if target >= letters[-1]:
            return letters[0]
        uniq_letters = [letters[0]]
        for c in letters[1:]:
            if c != uniq_letters[-1]:
                uniq_letters.append(c)
        # binary search
        lo, hi = 0, len(uniq_letters) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            c = uniq_letters[mid]
            if target == c:
                return uniq_letters[mid+1]
            elif target > c:
                lo = mid + 1
            else:
                hi = mid
        return uniq_letters[hi]

obj = Solution()
letters = ["c", "f", "j"]
target = "a"
print(obj.nextGreatestLetter(letters, target))
# Output: "c"

letters = ["c", "f", "j"]
target = "c"
print(obj.nextGreatestLetter(letters, target))
# Output: "f"

letters = ["c", "f", "j"]
target = "d"
print(obj.nextGreatestLetter(letters, target))
# Output: "f"

letters = ["c", "f", "j"]
target = "g"
print(obj.nextGreatestLetter(letters, target))
# Output: "j"

letters = ["c", "f", "j"]
target = "j"
print(obj.nextGreatestLetter(letters, target))
# Output: "c"

letters = ["c", "f", "j"]
target = "k"
print(obj.nextGreatestLetter(letters, target))
# Output: "c"

