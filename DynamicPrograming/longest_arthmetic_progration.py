def Solve(A):
    ans, n = 2, len(A)
    if n <= 2:
        return n
    llap = [2] * n
    A.sort()
    for j in range(n - 2, -1, -1):
        i, k = j - 1, j + 1
        while i >= 0 and k < n:
            if A[i] + A[k] == 2 * A[j]:
                llap[j] = max(llap[k] + 1, llap[j])
                ans = max(ans, llap[j])
                i, k = i - 1, k + 1
            elif A[i] + A[k] < 2 * A[j]:
                k += 1
            else:
                i -= 1
    return ans
a = [9, 4, 7, 6, 10, 13]
print(Solve(a))