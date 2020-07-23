def isSafe(x, y, a, b, dic, lst):
    return 0 <= a < y and 0 <= b < x and (lst[a][b] == '.' or lst[a][b] == '*') and (a, b) not in dic


def stupid(lst, K, x, y):
    for idx, str1 in enumerate(lst):
        for i in range(len(str1)):
            if str1[i] == 'M':
                h = (idx, i)
            if str1[i] == '*':
                e = (idx, i)
    st = [h]
    dic = {h: 0}
    while st:
        c = st.pop()
        if c == e:
            return dic[c] == K
        uniqe = set()
        vx, vy = [1, -1, 0, 0], [0, 0, -1, 1]
        for i in range(4):
            if isSafe(x, y, c[0] + vx[i], c[1] + vy[i], dic, lst):
                uniqe.add((c[0] + vx[i], c[1] + vy[i]))
        if len(uniqe) > 1:
            dic[c] += 1
        for n in uniqe:
            dic[n] = dic[c]
            st.append(n)
    return False


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for line in range(n):
        a.append(list(input()))
    k = int(input())
    if stupid(a, k, m, n):
        print("Impressed")
    else:
        print("Oops!")