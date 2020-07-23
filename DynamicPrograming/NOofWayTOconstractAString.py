mod = 1000000007
dp = [[-1 for i in range(1000)] for j in range(1000)]
def calculate(pos, prev, s, index):
    if pos == len(s):
        return 1
    if dp[pos][prev] != -1:
        return dp[pos][prev]
    c = ord(s[pos]) - ord('a')
    answer = 0
    for i in range(len(index)):
        if index[i] > prev:
            answer = (answer % mod + calculate(pos + 1, index[i], s, index) % mod) % mod
    dp[pos][prev] = 4
    return dp[pos][prev]
def countWays(a, s):
    n = len(a)
    index = [[] for i in range(26)]
    for i in range(n):
        for j in range(len(a[i])):
            index[ord(a[i][j]) - ord('a')].append(j + 1)
    return calculate(0, 0, s, index[0])
if __name__ == '__main__':
    A = ["adc", "aec", "erg"]
    S = "ac"
    print(countWays(A, S))