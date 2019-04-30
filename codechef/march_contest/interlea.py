import heapq as hp


def get_ints(string, idx):
    l = list()
    for x in string:
        l.append((int(x), idx))
    return l[::-1]


n = int(input())
s = list()
min_heaps = list()

for idx in range(n):
    l = get_ints(input(), idx)
    s.append(l)
    # hp.heapify(l)
    min_heaps.append(l)


# Make combined heap
comb_min_heap = list()
for each_min_heap in min_heaps:
    x = each_min_heap[-1]
    each_min_heap.pop()
    comb_min_heap.append(x)
hp.heapify(comb_min_heap)

# print(min_heaps)
for x in min_heaps:
    print(x)
print('\n\n')
print(comb_min_heap)

final_ans = list()
w = list()
# Repeat till combined heap is empty
while len(comb_min_heap):
    top = hp.heappop(comb_min_heap)
    str_idx = top[1]
    final_ans.append(str_idx)
    w.append(top[0])

    # Get root from min_heap[str_idx] if present and add it to combined heap
    if len(min_heaps[str_idx]):
        idx_top = min_heaps[str_idx].pop()
        hp.heappush(comb_min_heap, idx_top)

    print(comb_min_heap)


print("W = ", end='')
for x in w:
    print(x, end='')
print('\n')
score = 0
for i in range(2, len(w)):
    score += (w[i]-w[i-1])**2
print('\nScore: {}'.format(score))

for x in final_ans:
    print(x+1, end=' ')






"""
3
123
456
789

5
1238712136
7593292356
9273456952
2908203745
2328570825

"""