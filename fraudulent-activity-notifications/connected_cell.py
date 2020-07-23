ROW = int(input())
COL = int(input())
def isSafe(M, row, col, visited):
    return 0 <= row < ROW and 0 <= col < COL and (M[row][col] and not visited[row][col])
def stupid(M, row, col, visited, count):
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
    visited[row][col] = True
    for k in range(8):
        if isSafe(M, row + rowNbr[k], col + colNbr[k], visited):
            count[0] += 1
            stupid(M, row + rowNbr[k], col + colNbr[k], visited, count)
def yuck(M):
    global ROW, COL
    visited = [[False for j in range(COL)] for i in range(ROW)]
    ans = -1
    for i in range(ROW):
        for j in range(COL):
            if M[i][j] and not visited[i][j]:
                count = [1]
                stupid(M, i, j, visited, count)
                ans = max(ans, count[0])
    return ans
M = []
for _ in range(ROW):
    M.append(list(map(int, input().split(" "))))
print(yuck(M))