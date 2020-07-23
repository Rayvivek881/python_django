str1, str2 = input(), input()
n = len(str2)
mat = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if str2[i - 1] == str1[j - 1]:
            mat[i][j] = mat[i - 1][j - 1] + 1
        else:
            mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])
print(mat[-1][-1])