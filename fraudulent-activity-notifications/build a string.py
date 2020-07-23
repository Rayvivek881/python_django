for _ in range(int(input())):
    n, a, b = map(int, input().split(" "))
    text, lst = input(), [float("Inf")] * (n + 1)
    lst[0] = 0
    for i in range(1, n + 1):
        lst[i] = min(lst[i], lst[i - 1] + a)
        ans_str, j = text[:i], 0
        while j <= i and i + j < n + 1:
            if text[i: i + j] not in ans_str:
                break
            lst[i + j], j = min(lst[i + j], lst[i] + b), j + 1
    print(lst[n])