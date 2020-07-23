def stupid(s):
    c = len(s)
    n, l, r = len(s), 0, 0
    z = [0] * n
    for i in range(1, n):
        if i > r:
            l = r = i
            while r < n and s[r - l] == s[r]:
                r += 1
            z[i] = r - l
            r -= 1
            c += z[i]
        else:
            k = i - l
            if z[k] <= r - i + 1:
                z[i] = z[k]
                c += z[i]
            else:
                l = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                c += z[i]
                r -= 1
    return c
print(stupid("ababaa"))