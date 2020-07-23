def stupid(x, n):
    dp = [[0 for x in range(n)] for y in range(n)]
    p = [[False for x in range(n)] for y in range(n)]
    for i in range(n):
        p[i][i] = True
        if i + 1 < n and x[i] == x[i + 1]:
            p[i][i + 1] = True
            dp[i][i + 1] = 1
    for gap in range(2, n):
        for i in range(n - gap):
            j = gap + i
            if x[i] == x[j] and p[i + 1][j - 1]:
                p[i][j] = True
            if p[i][j]:
                dp[i][j] = dp[i][j - 1] + dp[i + 1][j] + 1 - dp[i + 1][j - 1]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]
    return dp[0][n - 1]


print(stupid('ghhggh', 6))