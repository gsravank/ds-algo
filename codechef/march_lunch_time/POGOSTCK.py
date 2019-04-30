for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    mod_lists = []
    for _ in range(k):
        mod_lists.append(list())

    curr_idx = n-1
    curr_max = None

    while curr_idx >= 0:
        if len(mod_lists[curr_idx % k]):
            prev = mod_lists[curr_idx % k][-1]
        else:
            prev = 0

        curr = prev + a[curr_idx]

        if curr_max is None:
            curr_max = curr
        else:
            if curr > curr_max:
                curr_max = curr

        mod_lists[curr_idx % k].append(curr)

        curr_idx -= 1

    print(curr_max)
    # print(mod_lists)


"""
2
5 2
3 6 4 7 2
5 3
3 -5 6 3 10

"""