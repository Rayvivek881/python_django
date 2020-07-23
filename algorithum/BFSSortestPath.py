from collections import *
for _ in range(int(input())):
    n, m = map(int, input().split(" "))
    lst = defaultdict(set)
    for i in range(n):
        lst[i + 1] = set()
    for i in range(m):
        a, b = map(int, input().split(" "))
        lst[a].add(b)
        lst[b].add(a)
    start = int(input())
    queue, val, visited = deque([start, 0]), {}, [start]
    while queue:
        a, cst = queue.popleft()
        for i in lst[a]:
            if i not in visited:
                visited.append(i)
                val[i] = 6 + cst
                queue.append(list(i, cst + 6))
    for i in lst:
        if i in val:
            print(val[i], end=' ')
        elif i != start:
            print('-1', end=' ')
    print()