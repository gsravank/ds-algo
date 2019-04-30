n = int(input())
a = list(map(int, input().strip().split()))

a = sorted(a)
# print(a)
max_size = 1

start = 0
end = 0

while start <= n-1:
    # print(start, end)
    while end <= n-1 and a[end] <= a[start] + 5:
        end += 1
    end -= 1
    curr_size = end - start + 1

    if curr_size > max_size:
        max_size = curr_size
    # print(start, end)
    # print('\n\n')
    # print(curr_size)
    # print('============')
    start += 1
    if end < start:
        end = start

print(max_size)