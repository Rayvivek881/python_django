def andOperator(x, y):
    res = 0
    while x > 0 and y > 0:
        msb_p1 = len(bin(x)[2:]) - 1
        msb_p2 = len(bin(y)[2:]) - 1
        if msb_p1 != msb_p2:
            break
        msb_val = (1 << msb_p1)
        res = res + msb_val
        x = x - msb_val
        y = y - msb_val
    return res


for _ in range(int(input())):
    a, b = map(int, input().split(" "))
    print(andOperator(a, b))