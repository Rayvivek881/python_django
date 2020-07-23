class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def storeInorder(root, inorder):
    if root is None:
        return
    storeInorder(root.left, inorder)
    inorder.append(root.data)
    storeInorder(root.right, inorder)


def countNodes(root):
    if root is None:
        return 0
    return countNodes(root.left) + countNodes(root.right) + 1


def arrayToBST(arr, root):
    if root is None:
        return
    arrayToBST(arr, root.left)
    root.data = arr[0]
    arr.pop(0)
    arrayToBST(arr, root.right)


def binaryTreeToBST(root):
    if root is None:
        return
    n = countNodes(root)
    arr = []
    storeInorder(root, arr)
    arr.sort()
    arrayToBST(arr, root)


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data)
    printInorder(root.right)


def printPostorder(root):
    if root is None:
        return
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.val)


def printPreorder(root):
    if root is None:
        return
    print(root.val),
    printPreorder(root.left)
    printPreorder(root.right)


def mirror(node):
    if node is None:
        return
    else:
        temp = node
        mirror(node.left)
        mirror(node.right)
        temp = node.left
        node.left = node.right
        node.right = temp


def height(node):
    if node is None:
        return 0
    else:
        lHeight = height(node.left)
        rHeight = height(node.right)
        return (lHeight + 1) if (lHeight > rHeight) else (rHeight + 1)


def getWidth(root, level):
    if root is None:
        return 0
    if level == 1:
        return 1
    elif level > 1:
        return getWidth(root.left,level-1) + getWidth(root.right,level-1)


def getMaxWidth(root):
    maxWidth = 0
    h = height(root)
    for i in range(1, h+1):
        width = getWidth(root, i)
        if width > maxWidth:
            maxWidth = width
    return maxWidth


root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right = Node(5)
binaryTreeToBST(root)

print("Following is the inorder traversal of the converted BST")
printInorder(root)