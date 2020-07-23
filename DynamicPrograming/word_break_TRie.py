def wordBreak(s, wordDict):
    class TrieNode():
        def __init__(self):
            self.children = []
            self.isLeaf = False
        def getNode(self):
            p = TrieNode()
            p.children = [None] * 26
            return p
        def insert(self, root, key):
            temp = root
            for i in key:
                index = ord(i) - ord('a')
                if temp.children[index] is None:
                    temp.children[index] = self.getNode()
                temp = temp.children[index]
            temp.isLeaf = True
        def search(self, root, key):
            temp = root
            for i in key:
                index = ord(i) - ord('a')
                if temp.children[index] is None:
                    return False
                temp = temp.children[index]
            if temp and temp.isLeaf:
                return True
    def checkWordBreak(s, root):
        n = len(s)
        if n == 0:
            return True
        for i in range(1, n + 1):
            if root.search(root, s[:i]) and checkWordBreak(s[i:], root):
                return True
        return False
    root = TrieNode().getNode()
    for w in wordDict:
        root.insert(root, w)
    return 'yes' if checkWordBreak(s, root) else 'no'
print(wordBreak("aaaaaaaa", ["aaa", "aaaab", 'aaaaa']))