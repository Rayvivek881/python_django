def get_median(c_s_l, t_d, m_p):
    counter, left = 0, 0
    while counter < m_p:
        counter += c_s_l[left]
        left += 1
    right = left
    left -= 1
    if counter > m_p or t_d % 2 != 0:
        return left
    else:
        while c_s_l[right] == 0:
            right += 1
        return (left + right) / 2


def activityNotefications(z, t_d):
    c_s_l = [0] * 201
    end = t_d
    for i in range(0, end):
        c_s_l[z[i]] += 1
    current = 0
    total_notefication = 0
    if t_d % 2 == 0:
        median_position = int(t_d / 2)
    else:
        median_position = int(t_d / 2) + 1
    total_notefication_length = len(z)
    while end < total_notefication_length:
        median = get_median(c_s_l, t_d, median_position)
        if z[end] >= median * 2:
            total_notefication += 1
        c_s_l[z[current]] -= 1
        c_s_l[z[end]] += 1
        current += 1
        end += 1
    return total_notefication


n, d = map(int, input().split(" "))
e = list(map(int, input().split(" ")))
print(activityNotefications(e, d))
