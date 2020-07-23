def stupid(a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def sharlockAnagums(s):
    count = 0
    for i in range(1, len(s)):
        a = ["".join(sorted(s[j:j + i])) for j in range(len(s) - i + 1)]
        b = stupid(a)
        for j in b:
            count += b[j] * (b[j] - 1) // 2
    return count