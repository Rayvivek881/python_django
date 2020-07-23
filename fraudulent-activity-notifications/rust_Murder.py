from collections import defaultdict
for _ in range(int(input())):
    n, e = map(int, input().split(" "))
    dists, roads = [1] * n, defaultdict(set)
    for _ in range(e):
        n1, n2 = map(int, input().split(" "))
        roads[n1].add(n2)
        roads[n2].add(n1)
    start_loc = int(input())
    not_visited, newly_visited, curr_dist = roads[start_loc], set(), 2
    while not_visited:
        for i in not_visited:
            if len(not_visited | roads[i]) < n:
                dists[i-1] = curr_dist
                newly_visited.add(i)
        not_visited -= newly_visited
        newly_visited, curr_dist = set(), curr_dist + 1
    del dists[start_loc-1]
    print(" ".join(map(str, dists)))