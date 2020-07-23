N = 10000
seg = [0] * (3 * N)
def update(In, l, r, up_In, val):
    if r < up_In or l > up_In:
        return seg[In]
    if l == up_In and r == up_In:
        seg[In] = val
        return val
    m = (l + r) // 2
    seg[In] = update(2 * In + 1, l, m, up_In, val) + update(2 * In + 2, m + 1, r, up_In, val)
    return seg[In]

def query(In, l, r, l1, r1):
    if l > r:
        return 0
    if r < l1 or l > r1:
        return 0
    if l1 <= l and r <= r1:
        return seg[In]
    m = (l + r) // 2
    return query(2 * In + 1, l, m, l1, r1) + query(2 * In + 2, m + 1, r, l1, r1)
def fIndCnt(arr, n):
    brr = [0] * n
    for i in range(n):
        brr[i] = arr[i]
    brr = sorted(brr)
    r = dict()
    for i in range(n):
        r[brr[i]] = i + 1
    dp = [0] * n
    ans = 0
    for i in range(n - 1, -1, -1):
        rank = r[arr[i]]
        dp[i] = 1 + query(0, 0, n - 1, rank, n - 1)
        ans += dp[i]
        update(0, 0, n - 1, rank - 1, dp[i] + query(0, 0, n - 1, rank - 1, rank - 1))
    return ans

arr = [1, 2, 10, 9]
n = len(arr)
print(fIndCnt(arr, n))