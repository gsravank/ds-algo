n = int(input())
a = list(map(int, input().strip().split()))

max_elem = max(a)
max_count = 1
curr_count = 0

for idx, elem in enumerate(a):
    if elem == max_elem:
        curr_count += 1
        if curr_count > max_count:
            max_count = curr_count
    else:
        curr_count = 0

    # print(curr_count)

print(max_count)