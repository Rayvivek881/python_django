def reverse(string, length, l, r):
    if l < 0 or r >= length or l > r:
        return string
    string = list(string)
    while l < r:
        string[l], string[r] = string[r],  string[l]
        l += 1
        r -= 1
    return "".join(string)


string = "geeksforgeeks"
length = len(string)
l = 5
r = 7
print(reverse(string, length, l, r))