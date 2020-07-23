from collections import deque
n, m = map(int, input().split(" "))
s1, s2, e1, e2 = map(int, input().split(" "))
mat = []
for _ in range(m):
    mat.append(list(map(int, list(input()))))


def printPath(arr, e1, e2):
    ans = [['0'] * n for _ in range(m)]
    while (e1, e2) != (-1, -1):
        ans[e1][e2] = '1'
        e1, e2 = arr[e1][e2]
    for i in ans:
        print(" ".join(i))


def isSafe(a, b, visited):
    return 0 <= a < m and 0 <= b < n and not visited[a][b] and mat[a][b]


def BFS(mat, s1, s2, e1, e2, m, n):
    visited, arr = [[False] * n for _ in range(m)],  [[0] * n for _ in range(m)]
    queue, visited[s1][s2], arr[s1][s2] = deque([(s1, s2, 0)]), True, (-1, -1)
    vx, vy = [0, 1, 0, -1], [1, 0, -1, 0]
    while queue:
        a, b, w = queue.popleft()
        if (a, b) == (e1, e2):
            return arr, w
        for i in range(4):
            if isSafe(a + vx[i], b + vy[i], visited):
                queue.append((a + vx[i], b + vy[i], w + 1))
                visited[a + vx[i]][b + vy[i]] = True
                arr[a + vx[i]][b + vy[i]] = (a, b)
    return visited, -1


arr, w = BFS(mat, s1, s2, e1, e2, m, n)
if w == -1:
    print("unreachable")
else:
    print(w, "stapsOnly")
    printPath(arr, e1, e2)