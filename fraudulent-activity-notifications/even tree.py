def dfs(tree, visit, ans, node):
    num = 0
    temp = 0
    visit[node] = 1
    for i in range(len(tree[node])):
        if not visit[tree[node][i]]:
            temp = dfs(tree, visit, ans, tree[node][i])
            if temp % 2:
                num += temp
            else:
                ans[0] += 1
    return num + 1


def minEdge(tree, n):
    visit = [0] * (n + 2)
    ans = [0]
    dfs(tree, visit, ans, 1)
    return ans[0]


n, m = map(int, input().split(" "))
tree = [[] for i in range(n + 2)]
for _ in range(m):
    a, b = map(int, input().split(" "))
    tree[a].append(b)
    tree[b].append(a)
print(minEdge(tree, n))