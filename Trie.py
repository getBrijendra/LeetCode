class TrieNode:
    def __init__(self) -> None:
        self.children = [None]*26
        self.isEoW = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def getIndex(self, c):
        return ord(c) - ord('a')

    def insert(self, key):
        n = len(key)
        curr = self.root
        for i in key:
            if curr.children[self.getIndex(i)] == None:
                curr.children[self.getIndex(i)] = TrieNode()
            curr = curr.children[self.getIndex(i)]
        curr.isEoW = True

    def search(self, key):
        n = len(key)
        curr = self.root
        for i in key:
            if curr.children[self.getIndex(i)] == None:
                return False
            curr = curr.children[self.getIndex(i)]
        return curr.isEoW
