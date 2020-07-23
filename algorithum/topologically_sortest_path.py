from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for node, weight in self.graph[v]:
            if not visited[node]:
                self.topologicalSortUtil(node, visited, stack)
        stack.append(v)

    def shortestPath(self, s):
        visited = [False] * self.V
        stack = deque([])

        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(s, visited, stack)
        dist = [float("Inf")] * self.V
        dist[s] = 0
        while stack:
            i = stack.pop()
            for node, weight in self.graph[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight
        print(" ".join(map(str, dist)))


g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, 1)
g.addEdge(4, 5, 2)
print("Following are shortest distances from source %d " % 1)
g.shortestPath(1)
