
for _ in range(int(input())):
    r, c = list(map(int, input().strip().split()))
    mat = list()
    all_nums = list(map(int, input().split()))

    for r_num in range(r):
        mat.append(all_nums[r_num*c: (r_num+1)*c])


    unreachable_one = False
    max_dist = 1

    # Row wise traversal
    for row in mat:
        pass

    # Col wise traversal


    if unreachable_one:
        print(-1)
    else:
        print(max_dist)
