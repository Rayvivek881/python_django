from collections import deque
for _ in range(int(input())):
    lst = {}
    for i in range(int(input())):
        a, b = map(int, input().split(" "))
        lst[a] = b
    for i in range(int(input())):
        a, b = map(int, input().split(" "))
        lst[a] = b
    queue, visited = deque([(1, 0)]), set()
    while queue:
        a, b = queue.popleft()
        if a == 100:
            break
        visited.add(a)
        for i in range(1, 7):
            if a + i not in visited and a + i <= 100:
                if a + i in lst:
                    queue.append((lst[a + i], b + 1))
                else:
                    queue.append((a + i, b + 1))
    if a != 100 and not queue:
        print('-1')
    elif a == 100:
        print(b)