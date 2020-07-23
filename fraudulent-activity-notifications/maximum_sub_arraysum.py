for _ in range(int(input())):
    n, m = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    sums = [-1] * n
    temp = [0] * 2
    temp[0] = arr[0] % m
    sums[0] = temp
    for i in range(1, n):
        temp = [-1] * 2
        temp[0] = (sums[i - 1][0] + (arr[i] % m)) % m
        temp[1] = i
        sums[i] = temp
    sums = sorted(sums)
    man = -1
    for i in range(0, n - 1):
        if sums[i][1] > sums[i + 1][1] and (sums[i + 1][0] - sums[i][0] < man or man == -1):
            man = sums[i + 1][0] - sums[i][0] 
    if sums[n - 1][0] > m - man:
        man = m - sums[n - 1][0]
    print(m - man)