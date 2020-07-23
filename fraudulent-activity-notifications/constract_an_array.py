def countArray(n, k, x):
    a, b = [0] * n, [0] * n
    if x == 1:
        a[0] = 1
    else:
        b[0] = 1
    for i in range(1, n):
        a[i] = b[i - 1] % 1000000007
        b[i] = ((a[i - 1] * (k - 1)) + (b[i - 1] * (k - 2))) % 1000000007
    return a[n - 1]