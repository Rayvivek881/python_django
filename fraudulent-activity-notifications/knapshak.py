for _ in range(int(input())):
    n, k = map(int, input().split(" "))
    lst = list(map(int, input().split(" ")))
    mat = [[0 for _ in range(k + 1)] for _ in range(2)]
    for i in range(n):
        for j in range(k + 1):
            if j == 0:
                mat[i%2][j] = 1
            elif i == 0:
                if j % lst[i] == 0:
                    mat[i%2][j] = 1
            else:
                if lst[i] > j:
                    mat[i%2][j] = mat[(i%2) - 1][j]
                else:
                    mat[i%2][j] = mat[(i%2) - 1][j] + mat[i%2][j - lst[i]]
    if n != 1:
        for i in range(1, k + 2):
            if mat[1][-i]:
                print(k - i + 1)
                break
    else:
        for i in range(1, k + 2):
            if mat[0][-i]:
                print(k - i + 1)
                break