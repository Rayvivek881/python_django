def combinationUtil(arr, n, r, index, data, i):
    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print(" ")
        return
    if i >= n:
        return
    data[index] = arr[i]
    combinationUtil(arr, n, r, index + 1, data, i + 1)
    combinationUtil(arr, n, r, index, data, i + 1)


def printcombination(arr, n, r):
    data = list(range(r))
    combinationUtil(arr, n, r, 0, data, 0)


arr = [10, 20, 30, 40, 50]
r = 3
n = len(arr)
printcombination(arr, n, r)