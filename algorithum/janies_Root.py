from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def jeanisRoute(k, roads, cities):
    g, start, cities = defaultdict(dict), cities[0], set(cities)
    for i, j, w in roads:
        g[i][j] = g[j][i] = w
    visited = set()
    ans = [0, 0]
    def dfs(node, dis=0):
        visited.add(node)
        isBelong = node in cities
        minus = [0, 0]
        for i, val in g[node].items():
            if i not in visited:
                d = dfs(i, dis + val) - dis
                if d > 0:
                    isBelong = True
                    ans[0] += 2 * g[node][i]
                    if d > minus[0]:
                        minus[1], minus[0] = max(minus), d
                    else:
                        minus[1] = max(minus[1], d)
        ans[1] = max(ans[1], sum(minus))
        return dis + max(minus) if isBelong else 0
    dfs(start)
    return ans[0] - ans[1]
n, k = map(int, input().split(" "))
cities = list(map(int, input().split(" ")))
roads = []
for _ in range(n - 1):
    roads.append(list(map(int, input().split(" "))))
print(jeanisRoute(k, roads, cities))