from collections import deque


def isSafe(r, c, n):
    return 0 <= r < n and 0 <= c < n


def stupid(a, b, n):
    queue = deque([(0, 0, 0)])
    drx, dcy = [a, -a, -a, a, b, -b, -b, b], [b, b, -b, -b, a, a, -a, -a]
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    while queue:
        a, b, depth = queue.popleft()
        depth += 1
        for i in range(8):
            new_r = a + drx[i]
            new_c = b + dcy[i]
            if isSafe(new_r, new_c, n) and not visited[new_r][new_c]:
                if new_r == n - 1 and new_c == n - 1:
                    return depth
                queue.append((new_r, new_c, depth))
                visited[new_r][new_c] = True
    return -1


n = int(input())
answer = [[0] * (n - 1) for _ in range(n - 1)]
for i in range(1, n):
    for j in range(i, n):
        answer[i - 1][j - 1] = stupid(i, j, n)
        answer[j - 1][i - 1] = answer[i - 1][j - 1]
for ans in answer:
    print(*ans)
