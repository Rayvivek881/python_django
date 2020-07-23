MAX = 256
freq = [[0 for i in range(MAX)] for j in range(MAX)]


def preCalculate(string, n):
    freq[ord(string[0])][0] = 1
    for i in range(1, n):
        ch = string[i]
        for j in range(MAX):
            charToUpdate = chr(j)
            if charToUpdate == ch:
                freq[j][i] = freq[j][i - 1] + 1
            else:
                freq[j][i] = freq[j][i - 1]


def getFrequency(ch, l, r):
    if l == 0:
        return freq[ord(ch)][r]
    else:
        return (freq[ord(ch)][r] -
                freq[ord(ch)][l - 1])


def firstNonRepeating(string, n, l, r):
    t = [""] * 2
    for i in range(l, r):
        ch = string[i]
        if getFrequency(ch, l, r) == 1:
            t[0] = ch
            return t[0]
    return "-1"


string = "GeeksForGeeks"
n = len(string)
queries = [(0, 3), (2, 3), (5, 12)]
q = len(queries)
preCalculate(string, n)
for i in range(q):
    print(firstNonRepeating(string, n, queries[i][0], queries[i][1]))
