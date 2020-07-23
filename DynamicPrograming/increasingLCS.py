def numberofways(A, B, N, M):
    pos, ans = [[] for _ in range(256)], 0
    for i in range(M):
        pos[ord(B[i])].append(i + 1)
    dpl, dpr = [[0] * (M + 2) for _ in range(N + 2)], [[0] * (M + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i - 1] == B[j - 1]:
                dpl[i][j] = dpl[i - 1][j - 1] + 1
            else:
                dpl[i][j] = max(dpl[i - 1][j], dpl[i][j - 1])
    for i in range(N, 0, -1):
        for j in range(M, 0, -1):
            if A[i - 1] == B[j - 1]:
                dpr[i][j] = dpr[i + 1][j + 1] + 1
            else:
                dpr[i][j] = max(dpr[i + 1][j], dpr[i][j + 1])
    for i in range(N + 1):
        for j in range(256):
            for x in pos[j]:
                if dpl[i][x - 1] + dpr[i + 1][x + 1] == dpl[N][M]:
                    ans += 1
                    break
    return ans


A = "aa"
B = "baaa"
print(numberofways(A, B, len(A), len(B)))