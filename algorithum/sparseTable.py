from math import log2
def buildSparseTable(arr, n):
    for i in range(0, n):
        table[i][0] = arr[i]
    j = 1
    while(1 << j) <= n:
        i = 0
        while(i + (1 << j) - 1) < n:
            table[i][j] = min(table[i][j - 1], table[i + (1 << (j - 1))][j - 1])
            i += 1
        j += 1
def query(L, R):
    j = int(log2(R - L + 1))
    return min(table[L][j], table[R - (1 << j) + 1][j])
a = [7, 2, 3, 0, 5, 10]
n = len(a)
table = [[0 for i in range(n)] for j in range(n)]
buildSparseTable(a, n)
print(query(0, 2))