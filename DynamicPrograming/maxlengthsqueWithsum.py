import numpy as np
def maxLengthSquare(row, column, arr, k):
    sam = np.zeros((row + 1, column + 1))
    cur_max = 1
    man = 0
    for i in range(1, row + 1):
        for j in range(1, column + 1):
            sam[i][j] = sam[i - 1][j] + sam[i][j - 1] + arr[i - 1][j - 1] - sam[i - 1][j - 1]
            if i >= cur_max and j >= cur_max and sam[i][j] - sam[i - cur_max][j] - sam[i][j - cur_max] + sam[i - cur_max][j - cur_max] <= k:
                man = cur_max
                cur_max += 1
    return man

if __name__ == "__main__":
    row = 4
    column = 4
    matrix = [[1, 1, 1, 1],
              [1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 0, 0, 0]]
    k = 6
    ans = maxLengthSquare(row, column, matrix, k)
    print(ans)