def cutRod(price, n):
    val = [0 for x in range(n + 1)]
    for i in range(1, n + 1):
        max_val = -float('Inf')
        for j in range(i):
            max_val = max(max_val, price[j] + val[i - j - 1])
        val[i] = max_val
    return val[n]
arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))