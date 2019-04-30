def read_items():
    return list(map(int, input().strip().split()))


n = int(input())
t = read_items()

change_points = [-1]
for idx in range(n-1):
    if t[idx+1] != t[idx]:
        change_points.append(idx)
change_points.append(n-1)

# print(change_points)

lengths = list()
for curr, next in zip(change_points[:-1], change_points[1:]):
    lengths.append(next-curr)

# print(lengths)

m = len(lengths)
max_len = 0
for idx in range(m-1):
    curr_max = min(lengths[idx], lengths[idx + 1])
    # print(curr_max)
    if curr_max > max_len:
        max_len = curr_max

print(2 * max_len)