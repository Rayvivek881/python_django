import sys
sys.setrecursionlimit(5000)
from collections import defaultdict
lst = defaultdict(list)


def DFS(lst, Visited, a, temp):
    Visited[a] = True
    temp.append(a)
    for i in lst[a]:
        if not Visited[i]:
            DFS(lst, Visited, i, temp)


def connectedComponents(lst, n):
    Visited, ans, count = [False] * n, [], 0
    for i in lst:
        if not Visited[i]:
            temp = []
            DFS(lst, Visited, i, temp)
            t = len(temp)
            ans.append(t)
            count += t
    if count < n:
        ans += [1] * (n - count)
    return ans


n, m = map(int, input().split(" "))
for _ in range(m):
    a, b = map(int, input().split(" "))
    lst[a].append(b)
    lst[b].append(a)
ans = connectedComponents(lst, n)
sam, result = 0, 0
for i in ans:
   result += sam * i
   sam += i
print(result)