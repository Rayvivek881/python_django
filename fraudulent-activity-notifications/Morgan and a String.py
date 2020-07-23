for _ in range(int(input())):
    str1, str2 = input() + 'z', input() + 'z'
    l_str1, l_str2 = len(str1), len(str2)
    while l_str1 > 1 and l_str2 > 1:
        if str1 < str2:
            print(str1[0], end="")
            str1 = str1[1:]
            l_str1 -= 1
        else:
            print(str2[0], end='')
            str2 = str2[1:]
            l_str2 -= 1
    if l_str1 != 1:
        print(str1[:l_str1 - 1])
    else:
        print(str2[:l_str2 - 1])