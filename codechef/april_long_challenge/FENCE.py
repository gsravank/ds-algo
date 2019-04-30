from collections import defaultdict


for _ in range(int(input())):
    n, m, k = list(map(int, input().strip().split()))

    row_map = defaultdict(lambda : dict())
    rc_list = list()
    for _ in range(k):
        r, c = list(map(int, input().strip().split()))
        row_map[r][c] = True# = row_map[r].union([c])
        rc_list.append((r, c))

    # print(row_map)
    total_fences = 0

    for rc_item in rc_list:
        r, c = rc_item
        if c-1 not in row_map[r]:
            total_fences += 1
        if c + 1 not in row_map[r]:
            total_fences += 1

        if r-1 in row_map:
            if c not in row_map[r-1]:
                total_fences += 1
            else:
                pass
        else:
            total_fences += 1

        if r+1 in row_map:
            if c not in row_map[r+1]:
                total_fences += 1
            else:
                pass
        else:
            total_fences += 1



    # for row in range(1, n+1):
    #     curr_cols = row_map[row]
    #     for col in curr_cols:
            #
            # if col < m and col + 1 not in curr_cols:
            #     total_fences += 1
            #
            # if col > 1 and col - 1 not in curr_cols:
            #     total_fences += 1
            #
            # if row < n and col not in row_map[row+1]:
            #     total_fences += 1
            #
            # if row > 1 and col not in row_map[row - 1]:
            #     total_fences += 1

            # if col + 1 not in curr_cols:
            #     total_fences += 1
            #
            # if col - 1 not in curr_cols:
            #     total_fences += 1
            #
            #
            # if col not in row_map[row + 1]:
            #     total_fences += 1
            #
            # if col not in row_map[row-1]:
            #     total_fences += 1

    print(total_fences)

"""
2
4 4 9
1 4
2 1 
2 2
2 3
3 1
3 3
4 1
4 2
4 3
4 4 1
1 1

"""