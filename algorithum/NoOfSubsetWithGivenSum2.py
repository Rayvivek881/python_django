def subsetSum(arr, n, i, sum, count):
    if i == n:
        if sum == 0:
            count += 1
        return count
    count = subsetSum(arr, n, i + 1, sum - arr[i], count)
    count = subsetSum(arr, n, i + 1, sum, count)
    return count


arr = [1, 2, 3, 4, 5]
sum = 10
n = len(arr)
print(subsetSum(arr, n, 0, sum, 0))