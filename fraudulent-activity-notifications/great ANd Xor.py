for _ in range(int(input())):
    x = int(input())
    print((1 << (len(bin(x)[2:]))) - 1 - x)