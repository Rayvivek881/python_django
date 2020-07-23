INT_BITS = 32
def leftRotate(n, d):
    return (n << d) | (n >> (INT_BITS - d))
def rightRotate(n, d):
    return (n >> d) | (n << (INT_BITS - d)) & 0xFFFFFFFF
n, d = 16, 2
print("Left Rotation of", n, "by", d, "is", leftRotate(n, d))
print("Right Rotation of", n, "by", d, "is", rightRotate(n, d))