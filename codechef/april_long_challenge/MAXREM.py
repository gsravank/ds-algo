n = int(input())
a = list(map(int, input().strip().split()))
a = sorted(a)

max_rem = -1
for idx in range(n-1):
    curr_max_rem = a[idx] % a[idx + 1]
    if curr_max_rem > max_rem:
        max_rem = curr_max_rem

print(max_rem)