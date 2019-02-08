n, k, m = list(map(int, input().split()))
a = list(map(int, input().split()))


sorted_a = sorted(a)

if m < n:
    rel_a = sorted_a[m:]
    avg = float(sum(rel_a)) / float(len(rel_a))
    print("%.10f" % avg)
else:
    last_num = sorted_a[-1]
    remaining_moves = m - (len(sorted_a) - 1)
    max_last_num = last_num + min(remaining_moves, k)
    print("%0.10f" % max_last_num)
