for _ in range(int(input())):
    n, lst = int(input()), list(map(int, input().split(" ")))
    max_arr, temp = [0] * n, lst[-1]
    for i in range(n - 1, -1, -1):
        if lst[i] <= temp:
            max_arr[i] = temp
        else:
            temp = lst[i]
            max_arr[i] = temp
    ans, temp = 0, 0
    for i in range(n):
        if lst[i] < max_arr[i]:
            temp += 1
            ans -= lst[i]
        elif lst[i] == max_arr[i]:
            ans += (lst[i] * temp)
            temp = 0
    print(ans)