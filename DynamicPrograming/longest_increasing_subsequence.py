def lis(arr):
    n = len(arr)
    las = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and las[i] < las[j] + 1:
                las[i] = las[j] + 1
    return max(las)


# o(nlog(n))
def CeilIndex(A, l, r, key):
    while r - l > 1:
        m = l + (r - l) // 2
        if A[m] >= key:
            r = m
        else:
            l = m
    return r


def LongestIncreasingSubsequenceLength(A, size):
    tailTable = [0 for i in range(size + 1)]
    tailTable[0] = A[0]
    len = 1
    for i in range(1, size):
        if A[i] < tailTable[0]:
            tailTable[0] = [i]
        elif A[i] > tailTable[len - 1]:
            tailTable[len] = A[i]
            len += 1
        else:
            tailTable[CeilIndex(tailTable, -1, len - 1, A[i])] = A[i]
    return len


A = [2, 5, 3, 7, 11, 8, 10, 13, 6]
n = len(A)

print("Length of Longest Increasing Subsequence is ", LongestIncreasingSubsequenceLength(A, n))
lst = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of lis is", lis(lst))