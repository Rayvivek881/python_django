def countFriendsPairings(n):
    a, b, c = 1, 2, 0
    if n <= 2:
        return n
    for i in range(3, n + 1):
        c = b + (i - 1) * a
        a = b
        b = c
    return c
def countFriendsPairings1(n):
    dp = [-1] * 10000
    if dp[n] != -1:
        return dp[n]
    if n > 2:
        dp[n] = (countFriendsPairings(n - 1) + (n - 1) * countFriendsPairings(n - 2))
        return dp[n]
    else:
        dp[n] = n
        return dp[n]
n = 3
print(countFriendsPairings(n))