def palindromeSubStrs(s, n):
    dp, m = [[0 for i in range(n)] for _ in range(n)], {}
    for i in range(n):
        dp[i][i] = 1
        m[s[i]] = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 1
            m[s[i: i + 2]] = 1
    for length in range(3, n + 1):
        for st in range(n - length + 1):
            end = st + length - 1
            if s[st] == s[end] and dp[st + 1][end - 1]:
                dp[st][end] = 1
                m[s[st: end + 1]] = 1
            else:
                dp[st][end] = 0
    return len(m), m, dp
s = "aacaa"
print(palindromeSubStrs(s, len(s)))