n, lst = int(input()), list(map(int, input().strip().split(" ")))
ans, tracker = [float('inf')] * n, [0] * n
ans[0], t, ans_path = 0, n - 1, [n]
for i in range(1, n):
    for j in range(i):
        if j + lst[j] >= i and ans[j] + 1 <= ans[i]:
            ans[i], tracker[i] = ans[j] + 1, j
while t != 0:
    ans_path.append(tracker[t] + 1)
    t = tracker[t]
print(ans[-1], 'StapsOnly')
print(" ".join(map(str, reversed(ans_path[:-1]))))