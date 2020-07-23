def distinctSubstring(P):
    S, N = dict(), len(P)
    for i in range(N):
        freq = [False] * 26
        s = ""
        for j in range(i, N):
            pos = ord(P[j]) - ord('a')
            if freq[pos]:
                break
            freq[pos] = True
            s += P[j]
            S[s] = 1
    return len(S), S


print(distinctSubstring("ababcabcabababd"))