from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def SCCUtil(self, u, low, disc, visited, st):
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        visited[u] = True
        st.append(u)
        for v in self.graph[u]:
            if disc[v] == -1:
                self.SCCUtil(v, low, disc, visited, st)
                low[u] = min(low[u], low[v])
            elif visited[v]:
                low[u] = min(low[u], disc[v])
        w = -1
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                print(w, end=" ")
                visited[w] = False
            print()

    def SCC(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        stackMember = [False] * self.V
        st = []
        for i in range(self.V):
            if disc[i] == -1:
                self.SCCUtil(i, low, disc, stackMember, st)


g4 = Graph(11)
g4.addEdge(0, 1)
g4.addEdge(0, 3)
g4.addEdge(1, 2)
g4.addEdge(1, 4)
g4.addEdge(2, 0)
g4.addEdge(2, 6)
g4.addEdge(3, 2)
g4.addEdge(4, 5)
g4.addEdge(4, 6)
g4.addEdge(5, 6)
g4.addEdge(5, 7)
g4.addEdge(5, 8)
g4.addEdge(5, 9)
g4.addEdge(6, 4)
g4.addEdge(7, 9)
g4.addEdge(8, 9)
g4.addEdge(9, 8)
print("SSC in graph ")
g4.SCC()