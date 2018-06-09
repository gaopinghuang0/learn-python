import unittest

# beats 21.26%
class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        # note: for each int, only the least significant 8 bits are used
        def least8bits(num):
            return bin(num)[2:][-8:].zfill(8)

        size = len(data)
        i = 0
        while i < size:
            num = data[i]
            # get the least significant 8 bits
            s = least8bits(num)
            # determine n-bytes char
            n = 0
            for j in s:
                if j == '1':
                    n += 1
                else:
                    break
            # print(n)
            if n > 4 or n == 1 or i+n > size:
                return False
            elif n == 0:
                i += 1
                continue
            # check the following n-1 bytes
            for j in range(i+1, n+i):
                num = data[j]
                s = least8bits(num)
                if not s.startswith('10'):
                    return False
            i += n
        return True



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        self.assertEqual(self.s.validUtf8([]), True)
        self.assertEqual(self.s.validUtf8([197]), False)
        self.assertEqual(self.s.validUtf8([145]), False)
        self.assertEqual(self.s.validUtf8([197, 130]), True)
        self.assertEqual(self.s.validUtf8([193, 156]), True)
        self.assertEqual(self.s.validUtf8([197, 130, 1]), True)
        self.assertEqual(self.s.validUtf8([197, 130, 1, 2]), True)
        self.assertEqual(self.s.validUtf8([235, 140, 4]), False)


if __name__ == "__main__":
    unittest.main()
