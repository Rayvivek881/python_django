def maxSubArraySum(a, size):
    max_so_far = -float("Inf")
    max_ending_here = 0
    ans = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
        if a[i] > 0:
            ans += a[i]
    if ans == 0:
        ans = max(a)
    return max_so_far
for _ in range(int(input())):
    n, lst = int(input()), list(map(int, input().split(" ")))
    print(maxSubArraySum(lst, n))