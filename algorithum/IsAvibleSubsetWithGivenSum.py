def stupid(lst, n, sam):
    mat = [[0 for i in range(sam + 1)] for j in range(n)]
    for i in range(n):
        mat[i][0] = 1
    for i in range(n):
        for j in range(1, sam + 1):
            if i == 0:
                if j == lst[i]:
                    mat[i][j] = 1
            elif lst[i] > j:
                mat[i][j] = mat[i - 1][j]
            else:
                mat[i][j] = mat[i - 1][j] or mat[i - 1][j - lst[i]]
    return "Yes" if mat[-1][-1] else "NO"


lst = [2, 3, 5, 7, 10]
print(stupid(lst, len(lst), 10))