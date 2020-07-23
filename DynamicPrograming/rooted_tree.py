p = []
adj = [0] * 10000
for i in range(10000):
    adj[i] = []
subtree_sum, visit, visit2 = [0] * 10000, [0] * 10000, [0] * 10000


def dfs1(root: int) -> int:
    if len(adj[root]) == 0:
        p[root][0] += p[root][1]
        return 0
    summ = 0
    for i in range(len(adj[root])):
        if visit[adj[root][i]] == 0:
            dfs1(adj[root][i])
            p[root][1] += p[adj[root][i]][1]
            visit[adj[root][i]] = 1
    p[root][0] += p[root][1]
    return 0


def dfs2(root: int) -> int:
    if len(adj[root]) == 0:
        subtree_sum[root] = p[root][0]
        return p[root][0]
    summ = p[root][0]
    for i in range(len(adj[root])):
        if visit2[adj[root][i]] == 0:
            summ += dfs2(adj[root][i])
            visit2[adj[root][i]] = 1
    subtree_sum[root] = summ
    return summ


if __name__ == "__main__":
    nodes, m, qu = 7, 4, 5
    a = [0, 1, 2, 2, 2, 1, 2]
    p.append([0, 0])
    for i in range(nodes):
        if a[i] != 0:
            adj[a[i]].append(i + 1)
        p.append([0, 0])
    v = [("ADD", [6, 76]), ("ADDUP", [1, 49]), ("ADD", [4, 48]), ("ADDUP", [2, 59])]
    for i in range(m):
        s = v[i][0]
        a = v[i][1][0]
        b = v[i][1][1]
        if s == "ADD":
            p[a][0] += b
        else:
            p[a][1] += b
    dfs1(1)
    dfs2(1)
    q = [["VALTREE", 1], ["VALTREE", 5], ["VAL", 5], ["VALTREE", 2], ["VAL", 2]]
    for i in range(qu):
        s = q[i][0]
        a = q[i][1]
        if s == "VAL":
            print(p[a][0])
        else:
            print(subtree_sum[a])
