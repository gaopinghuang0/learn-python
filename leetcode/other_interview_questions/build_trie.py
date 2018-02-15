# an easy way to build a trie using dict
# implementation learned from Discuss

words = ['asdf', '23rfasd', 'awdfjzc']

trie = {}
for w in words:
    t = trie
    for c in w:
        if c not in t:
            t[c] = {}
        t = t[c]
    t['#'] = '#'  # mark the end of word
print(trie)
