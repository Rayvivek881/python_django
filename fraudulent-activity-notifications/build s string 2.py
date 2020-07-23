def buildString(s, m):
    while m >= 2:
        if s[-m:] in s[:-m]:
            return m
        else:
            m -= 1
    return 1


for _ in range(int(input())):
    n, A, B = map(int, input().split(' '))
    S = input()
    minCost = 0
    while n > 2:
        x = n // 2
        k = buildString(S, x)
        if k != 1:
            minCost += B if A * k > B else A * k
        else:
            minCost += A
        n -= k
        string = S[:n]
    print(2 * A + minCost)