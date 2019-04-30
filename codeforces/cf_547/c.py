n = int(input())
q = list(map(int, input().strip().split()))

found_array = [False] * n
curr = 0

nums = list()
nums.append(curr)
found_array[curr] = True

max_n = curr
min_n = curr
excp = False

for qi in q:
    curr += qi
    nums.append(curr)
    try:
        found_array[curr] = True
    except Exception:
        # print("Exception")
        excp = True
        break

    if curr > max_n:
        max_n = curr

    if curr < min_n:
        min_n = curr


# print(nums)
# print(max_n)
# print(min_n)
# print(found_array)

# max_n = max(nums)
# min_n = min(nums)
if excp:
    print(-1)
else:
    if max_n - min_n + 1 == n and all(found_array):
        start_num = 1 - min_n
        print(start_num, end=' ')

        for qi in q:
            start_num += qi
            print(start_num, end=' ')
    else:
        print(-1)