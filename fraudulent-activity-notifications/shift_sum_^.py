n, k = map(int, input().split())
res, s = [0] * n, list(map(int, input()))
for i in range(n):
    if i == 0:
        res[0] = s[0]
    elif i < k:
        res[i] = s[i] ^ s[i - 1]
    else:
        res[i] = s[i] ^ s[i - 1] ^ res[i - k]
    print(res[i], end="")