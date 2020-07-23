from collections import defaultdict
import sys
sys.setrecursionlimit(10000)
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            try:
                u, v, w = self.graph[i]
                i = i + 1
                x = self.find(parent, u)
                y = self.find(parent, v)
                if x != y:
                    e = e + 1
                    result.append([u, v, w])
                    self.union(parent, rank, x, y)
            except:
                e += 1
        return result

visited = set()
n, m = map(int, input().split(" "))
g = Graph(n)
for _ in range(m):
    a, b, c = map(int, input().split(" "))
    g.addEdge(a - 1, b - 1, c)
lst = defaultdict(dict)
for a, b, c in g.KruskalMST():
    lst[a][b] = lst[b][a] = c
ans = []
def DFS(node, dis=0):
    if node == n - 1:
        ans.append(dis)
        return
    visited.add(node)
    for i, val in lst[node].items():
        if i not in visited and len(ans) == 0:
            if dis < val:
                DFS(i, val)
            else:
                DFS(i, dis)
    return
DFS(0)
if len(ans) == 0:
    print("NO PATH EXISTS")
else:
    print(ans[0])