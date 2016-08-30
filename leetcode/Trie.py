class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_word = True

    def search(self, word, is_word=True):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_word if is_word else True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.search(prefix, False)


# insert("abc"),search("abc"),search("ab"),insert("ab"),search("ab"),insert("ab"),search("ab")
# expected: [true,false,true,true]
trie = Trie()
trie.insert("abc")
print trie.search('abc')
print trie.search('ab')
print trie.insert('ab')
print trie.search('ab')


trie.insert('hello')
print trie.startsWith('wor')  == True
print trie.startsWith('mor')  == False
print trie.search('word') == True
print trie.search('hell') == False








