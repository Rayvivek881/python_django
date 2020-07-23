def maxProfit(profitA, profitB, n):
    preSum = [0] * n
    preSum[0] = profitA[0]
    for i in range(1, n):
        preSum[i] = preSum[i - 1] + profitA[i]
    suffSum = [0] * n
    suffSum[n - 1] = profitB[n - 1]
    for i in range(n - 2, -1, -1):
        suffSum[i] = suffSum[i + 1] + profitB[i]
    res = preSum[n - 1]
    for i in range(1, n - 1):
        res = max(res, preSum[i] + suffSum[i + 1])
    res = max(res, suffSum[0])
    return res


profitA = [2, 3, 2]
profitB = [10, 30, 40]
n = len(profitA)
print(maxProfit(profitA, profitB, n))
