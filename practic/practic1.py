import sys
from math import gcd
from collections import defaultdict
sys.setrecursionlimit(100000)
n, arr1 = int(input()), list(map(int, input().split(" ")))
arr2 = list(map(int, input().split(" ")))
garph, selected, ans, counter = defaultdict(set), {}, [], [0]
for i in range(n):
    for j in range(n):
        if gcd(arr1[i], arr2[j]) != 1:
            garph[arr1[i]].add(arr2[j])
            garph[arr2[j]].add(arr1[i])


def DFS(node, parent):
    counter[0] += 1
    print(counter[0])
    for i in garph[node]:
        if i not in selected and i != parent:
            DFS(i, node)
        if node not in garph:
            break
    if parent and node not in selected and parent not in selected:
        ans.append((node, parent))
        selected[node], selected[parent] = 1, 1
        del garph[node]
        del garph[parent]


for i in arr1:
    if i not in selected and i in garph:
        DFS(i, 0)
print(ans)