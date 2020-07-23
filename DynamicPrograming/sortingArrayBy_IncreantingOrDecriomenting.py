def getMinimumOps(lst, n):
    small, large = min(lst), max(lst)
    dp = [[0 for _ in range(large + 1)] for _ in range(n)]
    for j in range(small, large + 1):
        dp[0][j] = abs(lst[0] - j)
    for i in range(1, n):
        minimum = float('Inf')
        for j in range(small, large + 1):
            minimum = min(minimum, dp[i - 1][j])
            dp[i][j] = minimum + abs(lst[i] - j)
    return min(dp[n - 1][small:])
ar = [2, 4, 3, 6, 3]
print(getMinimumOps(ar, len(ar)))