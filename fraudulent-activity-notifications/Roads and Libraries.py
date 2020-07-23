from collections import defaultdict


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


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
    return len(ans)


for _ in range(int(input())):
    graph = defaultdict(set)
    No_cities, No_roads, C_lib, C_road = map(int, input().split(" "))
    for i in range(No_cities):
        graph[i] = set()
    parant, rank, No_Final_road = [], [0] * No_cities, 0
    for i in range(No_cities):
        parant.append(i)
    for i in range(No_roads):
        a, b = map(int, input().split(" "))
        x = find(parant, a - 1)
        y = find(parant, b - 1)
        if x != y:
            No_Final_road += 1
            graph[a - 1].add(b - 1)
            graph[b - 1].add(a - 1)
            union(parant, rank, x, y)
    min_lib = connectedComponents(graph, No_cities)
    a = (No_Final_road * C_road) + (min_lib * C_lib)
    b = No_cities * C_lib
    print(min(a, b))
