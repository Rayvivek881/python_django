# red knight shortest path __ hacker Rank
def get_val(val, dict1):
    for key, value in dict1.items():
        if val == value:
            return key


def printPath(arr, i, j):
    gg = {'UL': (2, 1), 'UR': (2, -1), 'R': (0, -2), 'LL': (-2, 1), 'LR': (-2, -1), 'L': (0, 2)}
    path = []
    while arr[i][j] != (-1, -1):
        path.append(get_val(arr[i][j], gg))
        ai, aj = gg[path[-1]]
        i, j = i + ai, j + aj
    for i in range(len(path)):
        print(path[-(i+1)], end=' ')


def IsInside(i, j):
    return 0 <= i < n and 0 <= j < n


def bfs(si, sj, ei, ej):
    visited = [[False] * n for _ in range(n)]
    track = [[0]*n for _ in range(n)]
    di = [-2, -2, 0, 2, 2, 0]
    dj = [-1, 1, 2, 1, -1, -2]
    queue = [(si, sj, 0)]
    visited[si][sj] = True
    track[si][sj] = (-1, -1)
    while queue:
        p = queue.pop(0)
        if p[0] == ei and p[1] == ej:
            return p[2], track
        for i in range(6):
            si, sj = p[0] + di[i], p[1] + dj[i]
            if IsInside(si, sj):
                if not visited[si][sj]:
                    queue.append((si, sj, p[2] + 1))
                    visited[si][sj] = True
                    track[si][sj] = (-di[i], -dj[i])
    return -1, visited


if __name__ == '__main__':
    n = int(input())
    si, sj, ei, ej = map(int, input().split(' '))
    dist, lst = bfs(si, sj, ei, ej)
    if dist == -1:
        print('Impossible')
    else:
        print(dist)
        printPath(lst, ei, ej)