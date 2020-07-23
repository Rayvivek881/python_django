def MatrixChainOrder(p, n):
    dp = [[0 for i in range(n)]
          for i in range(n)]
    for i in range(1, n):
        dp[i][i] = 0
    for L in range(1, n - 1):
        for i in range(n - L):
            dp[i][i + L] = min(dp[i + 1][i + L] + p[i - 1] * p[i] * p[i + L], dp[i][i + L - 1] + p[i - 1] * p[i + L - 1] * p[i + L])
    return dp[1][n - 1]


arr = [10, 20, 30, 40, 30]
size = len(arr)
print("Minimum number of multiplications is", MatrixChainOrder(arr, size))