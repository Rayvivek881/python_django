def get_longest_palindromes(strng):
    N, ans = len(strng), []
    for i in range(N, 0, -1):
        found = False
        for s in range(N - i + 1):
            target = strng[s:s + i]
            if target == target[::-1]:
                ans.append(i)
                found = True
        if found:
            break
    return ans if strng else 0


print(get_longest_palindromes("abaabc")[0])
