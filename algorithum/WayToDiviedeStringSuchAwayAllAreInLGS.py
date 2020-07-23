N = 2


def isVowel(ch):
    return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'


def performQueries(str1, len1, queries, q):
    pre = [0 for i in range(len1)]
    if isVowel(str1[0]):
        pre[0] = 1
    else:
        pre[0] = 0
    for i in range(0, len1, 1):
        if isVowel(str1[i]):
            pre[i] = 1 + pre[i - 1]
        else:
            pre[i] = pre[i - 1]
    for i in range(q):
        if queries[i][0] == 0:
            print(pre[queries[i][1]])
        else:
            print(pre[queries[i][1]] -
                  pre[queries[i][0] - 1])


str1 = "geeksforgeeks"
len1 = len(str1)
queries = [[1, 3], [2, 4], [1, 9]]
q = len(queries)
performQueries(str1, len1, queries, q)