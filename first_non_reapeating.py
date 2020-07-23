x, d = input(), {}
for i in x:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in x:
    if d[i] == 1:
        print(i)
        break