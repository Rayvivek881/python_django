def initialize(n):
    global Arr, size
    for i in range(n + 1):
        Arr[i] = i
        size[i] = 1


def find(i):
    global Arr, size
    while Arr[i] != i:
        Arr[i] = Arr[Arr[i]]
        i = Arr[i]
    return i


def _union(xr, yr):
    global Arr, size
    if size[xr] < size[yr]:
        Arr[xr] = Arr[yr]
        size[yr] += size[xr]
    else:
        Arr[yr] = Arr[xr]
        size[xr] += size[yr]


def isCycle(adj, V):
    global Arr, size
    for i in range(V):
        for j in range(len(adj[i])):
            x = find(i)
            y = find(adj[i][j])
            if x == y:
                return True
            _union(x, y)
    return False


MAX_VERTEX = 101
Arr = [None] * MAX_VERTEX
size = [None] * MAX_VERTEX

V = 3
initialize(V)
adj = [[] for i in range(V)]

adj[0].append(1)
adj[0].append(2)
adj[1].append(2)
if isCycle(adj, V):
    print("Graph contains Cycle.")
else:
    print("Graph does not contain Cycle.")