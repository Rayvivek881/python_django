for _ in range(int(input())):
    L, R = map(int, input().split(" "))
    s, arr = 0, list(map(int, input().split(" ")))
    for i in range(L, R + 1):
        s += arr[i]
    print("Sum of", [L, R], "is", s)