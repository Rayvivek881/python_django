class Node:
    def __init__(self, length=None, suffixEdge=None):
        self.start = None
        self.end = None
        self.length = length
        self.insertionEdge = [0] * 26
        self.suffixEdge = suffixEdge

def insert(currIndex):
    global currNode, ptr
    temp = currNode
    while True:
        currLength = tree[temp].length
        if currIndex - currLength > 0 and (s[currIndex] == s[currIndex - currLength - 1]):
            break
        temp = tree[temp].suffixEdge
    if tree[temp].insertionEdge[ord(s[currIndex]) - ord('a')] != 0:
        currNode = tree[temp].insertionEdge[ord(s[currIndex]) - ord('a')]
        return
    ptr += 1
    tree[temp].insertionEdge[ord(s[currIndex]) - ord('a')] = ptr
    tree[ptr].end = currIndex
    tree[ptr].length = tree[temp].length + 2
    tree[ptr].start = (tree[ptr].end - tree[ptr].length + 1)
    currNode = ptr
    temp = tree[temp].suffixEdge
    if tree[currNode].length == 1:
        tree[currNode].suffixEdge = 2
        return
    while True:
        currLength = tree[temp].length
        if currIndex - currLength >= 1 and s[currIndex] == s[currIndex - currLength - 1]:
            break
        temp = tree[temp].suffixEdge
    tree[currNode].suffixEdge = tree[temp].insertionEdge[ord(s[currIndex]) - ord('a')]

MAXN = 100
root1 = Node(-1, 1)
root2 = Node(0, 1)
tree = [Node() for _ in range(MAXN)]
currNode, ptr = 1, 2
tree[1] = root1
tree[2] = root2
s = "aaaaabbbbaaaa"
for i in range(len(s)):
    insert(i)
for i in range(tree[ptr].start, tree[ptr].end + 1):
    print(s[i], end="")