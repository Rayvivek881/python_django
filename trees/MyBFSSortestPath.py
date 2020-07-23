from collections import deque
R, C = map(int, input().split(" "))
queue = deque([])
def isSafe(M, row, col, visited):
    return 0 <= row < R and 0 <= col < C and M[row][col] and not visited[row][col]
t = []
def stupid(mat, c, d, visited):
    a1, b1, s = queue.popleft()
    if a1 == c and b1 == d:
        queue.clear()
        t.append(s)
        return
    av, bv = [-1, 1, 0, 0], [0, 0, 1, -1]
    for i in range(4):
        if isSafe(mat, a1 + av[i], b1 + bv[i], visited):
            queue.append([a1 + av[i], b1 + bv[i], s + 1])
            visited[a1 + av[i]][b1 + bv[i]] = True
    while queue:
       stupid(mat, c, d, visited)
def yuck(mat):
    a, b, visited = 0, 0, [[False for i in range(C)] for _ in range(R)]
    queue.append([a, b, 0])
    visited[a][b] = True
    stupid(mat, 3, 3, visited)
    return t[0] if len(t) >= 1 else "None"
mat = []
for _ in range(R):
    mat.append(list(map(int, input().split(" "))))
print(yuck(mat))