for _ in range(int(input())):
    n, lst= int(input()), list(map(int, input().split(" ")))
    dp = [[0, 0] for _ in range(n)]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + abs(lst[i - 1] - 1))
        dp[i][1] = max(dp[i - 1][0] + abs(lst[i] - 1), dp[i - 1][1])
    print(max(dp[n - 1]))