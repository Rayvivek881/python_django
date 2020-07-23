l1, len_l1, d = [], 0, {}
for i in range(int(input())):
    a = input()
    n = len(a)

    for j in range(n):
        for k in range(j+1, n+1):
            if a[j:k] not in d:
                l1.append(a[j:k])
                d[a[j:k]] = 1
                len_l1 += 1
l1 = sorted(l1)
d.clear()
for d in range(int(input())):
    x = int(input())
    if x > len_l1:
        print('INVALID')
    else:
        print(str(l1[x-1]))