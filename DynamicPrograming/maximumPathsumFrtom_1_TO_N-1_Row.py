N = 4
def MaximumPath(Mat):
    result = 0
    dp = [[0 for i in range(N + 2)] for j in range(N)]
    for i in range(N):
        for j in range(1, N + 1):
            dp[i][j] = max(dp[i - 1][j - 1],
                           max(dp[i - 1][j],
                               dp[i - 1][j + 1])) + \
                       Mat[i][j - 1]
    for i in range(N + 1):
        result = max(result, dp[N - 1][i])
    return result
Mat = [[4, 2, 3, 4],
       [2, 9, 1, 10],
       [15, 1, 3, 0],
       [16, 92, 41, 44]]
print(MaximumPath(Mat))