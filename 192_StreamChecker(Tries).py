# Create a trie node
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

# create a Trie
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in range(len(word) - 1, -1, -1):
            ch = word[i]
            if node.children[ord(ch) - ord('a')] == None:
                node.children[ord(ch) - ord('a')] = TrieNode()
            node = node.children[ord(ch) - ord('a')]

        node.isWord = True
class StreamChecker:
    trie = None
    string = None

    def __init__(self, words):
        StreamChecker.trie = Trie()
        StreamChecker.string = ''

        for word in words:
            self.trie.insert(word)

    def query(self, letter: str) -> bool:
        StreamChecker.string += letter
        return self.find()

    def find(self):
        node = StreamChecker.trie.root

        for i in range(len(StreamChecker.string) - 1, -1, -1):
            ch = StreamChecker.string[i]
            if node.isWord == True:
                return True
            if node.children[ord(ch) - ord('a')] == None:
                return False

            node = node.children[ord(ch) - ord('a')]

        return node.isWord

# Your StreamChecker object will be instantiated and called as such:
words = ["cd","f","kl"]
obj = StreamChecker(words)
print(obj.query('a'))
print(obj.query('b'))
print(obj.query('c'))
print(obj.query('d'))
print(obj.query('e'))
print(obj.query('f'))
print(obj.query('g'))
print(obj.query('h'))
print(obj.query('i'))
print(obj.query('j'))
print(obj.query('k'))
print(obj.query('l'))