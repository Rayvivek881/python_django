def largestSubset(a, n):
    a.sort()
    dp = [0 for i in range(n)]
    dp[n - 1] = 1
    for i in range(n - 2, -1, -1):
        mxm = 0
        for j in range(i + 1, n):
            if a[j] % a[i] == 0:
                mxm = dp[j]
                break
        dp[i] = 1 + mxm
    return max(dp)
a = [1, 3, 6, 13, 17, 24, 12]
print(largestSubset(a, len(a)))