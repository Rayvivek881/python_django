import sys
sys.setrecursionlimit(1000000)


def getNode():
    class Node:
        Children = []

    p = Node()
    p.Children = [None] * 26
    return p


def insert(s, node):
    if len(s) > 0:
        index = ord(s[0]) - ord('a')
        if node.Children[index] is None:
            node.Children[index] = getNode()
        insert(s[1:], node.Children[index])


def countNode(node):
    if node is None:
        return 0
    count = 0
    for i in range(26):
        if node.Children[i] is not None:
            count += countNode(node.Children[i])
    return count + 1


def search(node, s):
    if len(s) == 0:
        return True
    index = ord(s[0]) - ord('a')
    if node.Children[index] is None:
        return False
    else:
        return search(node.Children[index], s[1:])


root, a = getNode(), input()
for i in range(len(a)):
    insert(a[i:], root)
print('Count of distinct substrings is ', countNode(root) - 1)