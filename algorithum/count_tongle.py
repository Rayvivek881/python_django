MAX = 100000
tree = [0] * MAX
lazy = [False] * MAX


def toggle(node: int, st: int, en: int, us: int, ue: int):
    if lazy[node]:
        lazy[node] = False
        tree[node] = en - st + 1 - tree[node]
        if st < en:
            lazy[node << 1] = not lazy[node << 1]
            lazy[1 + (node << 1)] = not lazy[1 + (node << 1)]
    if st > en or us > en or ue < st:
        return
    if us <= st and en <= ue:
        tree[node] = en - st + 1 - tree[node]
        if st < en:
            lazy[node << 1] = not lazy[node << 1]
            lazy[1 + (node << 1)] = not lazy[1 + (node << 1)]
        return
    mid = (st + en) // 2
    toggle((node << 1), st, mid, us, ue)
    toggle((node << 1) + 1, mid + 1, en, us, ue)
    if st < en:
        tree[node] = tree[node << 1] + tree[(node << 1) + 1]


def countQuery(node: int, st: int, en: int, qs: int, qe: int) -> int:
    if st > en or qs > en or qe < st:
        return 0
    if lazy[node]:
        lazy[node] = False
        tree[node] = en - st + 1 - tree[node]
        if st < en:
            lazy[node << 1] = not lazy[node << 1]
            lazy[(node << 1) + 1] = not lazy[(node << 1) + 1]
    if qs <= st and en <= qe:
        return tree[node]
    mid = (st + en) // 2
    return countQuery((node << 1), st, mid, qs, qe) + countQuery(
        (node << 1) + 1, mid + 1, en, qs, qe)


n = 5
toggle(1, 0, n - 1, 1, 2)
toggle(1, 0, n - 1, 2, 4)
print(countQuery(1, 0, n - 1, 2, 3))
toggle(1, 0, n - 1, 2, 4)
print(countQuery(1, 0, n - 1, 1, 4))
