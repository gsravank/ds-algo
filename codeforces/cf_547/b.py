n = int(input())
a = list(map(int, input().strip().split()))


one_chunks = list()
idx = 0

curr_count = 0
for ai in a:
    if ai == 1:
        curr_count += 1
    else:
        one_chunks.append(curr_count)
        curr_count = 0
if a[-1] == 1:
    one_chunks.append(curr_count)

max_in_a_day = max(one_chunks)
if a[0] == 1:
    start_chunk = one_chunks[0]
else:
    start_chunk = 0

if a[-1] == 1:
    end_chunk = one_chunks[-1]
else:
    end_chunk = 0

# print(one_chunks)

print(max(max_in_a_day, end_chunk + start_chunk))
