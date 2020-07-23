def minCost(n, x, y, z):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        if i & 1:
            dp[i] = min(dp[(i + 1) // 2] + x + z, dp[i - 1] + y)
        else:
            dp[i] = min(dp[i // 2] + x, dp[i - 1] + y)
    return dp[n]


n, x, y, z = 15, 2, 1, 3
print(minCost(n, x, y, z))
