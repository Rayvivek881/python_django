def stupid(strr, k):
    palin = strr
    l = 0
    r = len(strr) - 1
    lst = []
    while l < r:
        if strr[l] != strr[r]:
            palin[l] = palin[r] = max(strr[l], strr[r])
            k -= 1
            lst.append([l, r])
        l += 1
        r -= 1
    if k < 0:
        return "-1"
    for i, j in lst:
        if k <= 0:
            break
        if palin[i] != '9':
            palin[i] = palin[j] = '9'
            k -= 1
    l = 0
    r = len(strr) - 1
    while l <= r:
        if l == r:
            if k > 0:
                palin[l] = '9'
        elif palin[l] < '9':
            if k >= 2 and palin[l] != strr[l] and palin[r] != strr[r]:
                k -= 1
                palin[l] = palin[r] = '9'
            elif k >= 2 and palin[l] == strr[l] and palin[r] == strr[r]:
                k -= 2
                palin[l] = palin[r] = '9'
        l += 1
        r -= 1
    return palin


n, k = map(int, input().split(" "))
strr = list(input())
a = stupid(strr, k)
print("".join(a))