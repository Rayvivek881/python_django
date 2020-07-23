count = []


def stupid(arr1, n1, r1, index, data, i):
    count.append(1)
    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print(" ")
        return
    if i >= n1:
        return
    data[index] = arr1[i]
    stupid(arr1, n1, r, index + 1, data, i + 1, )
    stupid(arr1, n1, r, index, data, i + 1, )


arr = list(input())
n, r = len(arr), int(input())
stupid(arr, n, r, 0, list(range(r)), 0)
print(len(count))