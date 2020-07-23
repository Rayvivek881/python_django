n, arr = int(input()), list(map(int, input().split()))
q, queries = int(input()), list(map(int, input().split()))
count = [0] * 7
for i in arr:
    count[3 + i] += 1
sum_num_right = [n]
for i in range(6):
    sum_num_right.append(sum_num_right[i] - count[i])
sum_right = [0] * 7
for i in range(7):
    sum_right[0] += count[i] * i
for i in range(1, 7):
    sum_right[i] = sum_right[i - 1] - sum_num_right[i]
sum_left = [0] * 7
for i in range(6, -1, -1):
    sum_left[6] += count[i] * (6 - i)
for i in range(5, -1, -1):
    sum_left[i] = sum_left[i + 1] - (n - sum_num_right[i + 1])
acc = 0
for i in queries:
    acc += i
    mid = 3 - acc
    if 7 > mid >= 0:
        print(sum_right[mid] + sum_left[mid])
    elif mid < 0:
        print(sum_right[0] + n * abs(mid))
    else:
        print(sum_left[6] + n * (mid - 6))