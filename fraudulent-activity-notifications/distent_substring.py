x, d = input(), {}
for i in range(len(x)):
    for j in range(i + 1, len(x) + 1):
        if x[i:j] not in d:
            d[x[i:j]] = 1
        else:
            d[x[i:j]] += 1
a = 0
for i in d:
    x = len(i) * d[i]
    if x > a:
        a = x
print(a)