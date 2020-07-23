def editDistance(str3, str4, m, n):
    lst = [[0 for _ in range(m + 1)] for _ in range(2)]
    for i in range(m + 1):
        lst[0][i] = i
    for i in range(1, n + 1):
        for j in range(m + 1):
            if j == 0:
                lst[i % 2][j] = i
            elif str4[i - 1] == str3[j - 1]:
                lst[i % 2][j] = lst[(i - 1) % 2][j - 1]
            else:
                lst[i % 2][j] = 1 + min(lst[(i - 1) % 2][j], lst[i % 2][j - 1], lst[(i - 1) % 2][j - 1])
    return lst[n % 2][m]


str1 = "abcdef"
str2 = "azced"
print(editDistance(str1, str2, len(str1), len(str2)))