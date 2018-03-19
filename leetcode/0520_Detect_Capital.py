# beats 27.45%
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 1:
            return True

        is_first_cap = word[0].isupper()
        if is_first_cap:  # all upper or all lower for word[1:]
            if word[1].isupper():
                for c in word[2:]:
                    if c.islower():
                        return False
            else:
                for c in word[2:]:
                    if c.isupper():
                        return False
        else:
            for c in word[1:]:
                if c.isupper():
                    return False
        return True
