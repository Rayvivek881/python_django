def longestCommonSubstring(S, T):
    if len(S) < len(T):
        S, T = T, S
    row = [0] * (len(T) + 1)
    longest = 0
    for si in S:
        for j, tj in enumerate(reversed(T)):
            k = len(T) - j
            if si == tj:
                row[k] = row[k-1] + 1
                if row[k] > longest:
                    longest = row[k]
    return longest, row


s, t = "aabcdd",  "dabcda"
print(longestCommonSubstring(s, t))