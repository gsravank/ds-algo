import heapq


n = int(input())
a = list(map(int, input().split()))

parity_map = {0: [], 1: []}
for ai in a:
    parity_map[ai % 2].append(ai)

odd_len = len(parity_map[1])
even_len = len(parity_map[0])

min_heap = list()

if abs(odd_len - even_len) <= 1:
    print(0)
else:
    if odd_len > even_len:
        rem_len = odd_len - even_len - 1
        rel_elems = parity_map[1]
    else:
        rem_len = even_len - odd_len - 1
        rel_elems = parity_map[0]


    heapq.heapify(rel_elems)
    # print(rel_elems)

    ans = 0
    for _ in range(rem_len):
        curr = heapq.heappop(rel_elems)
        ans += curr
    print(ans)

    # print(rel_elems)

"""
10
2 1 3 5 7 9 11 13 15 17

"""