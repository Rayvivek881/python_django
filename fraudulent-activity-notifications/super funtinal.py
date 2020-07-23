def unique_substring(x):
    d = {}
    for i in range(len(x)):
        for j in range(i + 1, len(x) + 1):
            d[x[i:j]] = j - i
    return d


for _ in range(int(input())):
    d, real_ans = unique_substring(input()), 0
    for i in d:
        l, u, ans = d[i], len(set(i)), 1
        for i in range(u):
            ans = (ans * l) % (1000000000 + 7)
        real_ans = (real_ans + ans) % (1000000000 + 7)
    print(real_ans % (1000000000 + 7))