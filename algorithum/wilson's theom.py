def f(x):
    if x == 0:
        return 1
    else:
        total = 1
        while x > 0:
            total *= x
            x -= 1
        return total


def wilson(x):
    if f(x - 1) % x == (x - 1) and x != 1:
        return 1
    else:
        return 0


a = input()
b = a.split(" ")
c = int(b[0])
d = int(b[1])
for i in range(c, d + 1):
    if wilson(i) == 1:
        print("{0}".format(i))