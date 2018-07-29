import unittest

# beats 30.70%
class Codec:
    short_long = {}
    long_short = {}
    cnt = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in Codec.long_short:
            return Codec.long_short[longUrl]
        else:
            Codec.cnt += 1
            short = str(Codec.cnt)
            Codec.long_short[longUrl] = short
            Codec.short_long[short] = longUrl
            return short

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return Codec.short_long[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Codec()

    def test_method(self):
        """Such as self.assertEqual, self.assertTrue"""
        longUrl = "https://leetcode.com/problems/design-tinyurl"
        self.assertEqual(self.s.decode(self.s.encode(longUrl)), longUrl)
        self.assertEqual(self.s.decode(self.s.encode(longUrl)), longUrl)
        longUrl = "https://leetcode.com/problems/design-tinyurl1"
        self.assertEqual(self.s.decode(self.s.encode(longUrl)), longUrl)


if __name__ == "__main__":
    unittest.main()
