class Node:
    def __init__(self):
        self.children = dict()
        self.isend = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i in cur.children.keys():
                cur = cur.children[i]
            else:
                cur.children[i] = Node()
                cur = cur.children[i]
        cur.isend = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if i in cur.children.keys():
                cur = cur.children[i]
            else:
                return False

        return cur.isend

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if i in cur.children.keys():
                cur = cur.children[i]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)