n, arr = int(input()), list(map(int, input().split()))
q, queries = int(input()), list(map(int, input().split()))
count = [0] * 4001
for i in arr:
    count[2000 + i] += 1
sum_num_right = [n]
for i in range(4000):
    sum_num_right.append(sum_num_right[i] - count[i])
sum_right = [0] * 4001
sum_right[0] = sum(arr) + (n * 2000)
for i in range(1, 4001):
    sum_right[i] = sum_right[i - 1] - sum_num_right[i]
sum_left = [0] * 4001
for i in range(4000, -1, -1):
    sum_left[4000] += count[i] * (4000 - i)
for i in range(3999, -1, -1):
    sum_left[i] = sum_left[i + 1] - (n - sum_num_right[i + 1])
acc = 0
for i in queries:
    acc += i
    mid = 2000 - acc
    if 4001 > mid >= 0:
        print(sum_right[mid] + sum_left[mid], end=" ")
    elif mid < 0:
        print(sum_right[0] + n * abs(mid), end=" ")
    else:
        print(sum_left[4000] + n * (mid - 4000), end=" ")