MAX = 10
def numToVec(N):
    digit = []
    while N != 0:
        digit.append(N % 10)
        N = N // 10
    if not digit:
        digit.append(0)
    digit = digit[::-1]
    return digit

def solve(A, B, C):
    d, d2 = 0, 0
    digit = numToVec(C)
    d = len(A)
    if B > len(digit) or d == 0:
        return 0
    elif B < len(digit):
        if A[0] == 0 and B != 1:
            return (d - 1) * pow(d, B - 1)
        else:
            return pow(d, B)
    else:
        dp = [0 for i in range(B + 1)]
        lower = [0 for i in range(MAX + 1)]
        for i in range(d):
            lower[A[i] + 1] = 1
        for i in range(1, MAX + 1):
            lower[i] = lower[i - 1] + lower[i]
        flag = True
        dp[0] = 0
        for i in range(1, B + 1):
            d2 = lower[digit[i - 1]]
            dp[i] = dp[i - 1] * d
            if i == 1 and A[0] == 0 and B != 1:
                d2 = d2 - 1

            if flag:
                dp[i] += d2
            flag = (flag & (lower[digit[i - 1] + 1] == lower[digit[i - 1]] + 1))
        return dp[B]
A = [0, 1, 2, 5]
N = 2
k = 21

print(solve(A, N, k))