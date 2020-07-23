from collections import defaultdict
lst = defaultdict(set)


def DFS(lst, Visited, a, temp):
    Visited[a] = True
    temp.append(a)
    for i in lst[a]:
        if not Visited[i]:
            DFS(lst, Visited, i, temp)


def connectedComponents(lst, n):
    Visited, ans = [False] * n, []
    for i in lst:
        if not Visited[i]:
            temp = []
            DFS(lst, Visited, i, temp)
            ans.append(temp)
    return ans


n, m = map(int, input().split(" "))
for _ in range(m):
    a, b = map(int, input().split(" "))
    lst[a].add(b)
    lst[b].add(a)
print(lst)