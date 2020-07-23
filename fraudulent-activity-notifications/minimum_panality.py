from collections import defaultdict, deque
graph = defaultdict(list)
n, m = map(int, input().split(" "))
for _ in range(m):
    u, v, c = map(int, input().split(" "))
    graph[u].append((v, c))
    graph[v].append((u, c))
start, end = map(int, input().split(" "))
lst, distance = deque([(start, 0)]), [dict() for _ in range(n + 1)]
ans = [float('inf')] * (n + 1)
while lst:
    a, d = lst.pop()
    for i, w in graph[a]:
        if d | w not in distance[i]:
            lst.append((i, d | w))
            distance[i][d | w] = 1
            ans[i] = min(ans[i], d | w)
print(ans[end] if distance[end] else "-1")