from collections import defaultdict


def cut_possible(row_counts, col_counts, per_row_strip_count, per_col_strip_count, choc_chip, R, C, H, V, each_piece_count):
    # for row in choc_chip:
    #     print(row)
    row_to_hor_cut_map = dict()
    col_to_ver_cut_map = dict()

    # Check horizontal/row strips
    curr_row_total = 0
    curr_row_num = 0
    for idx, row_count in enumerate(row_counts):
        curr_row_total += row_count
        row_to_hor_cut_map[idx] = curr_row_num

        if curr_row_total < per_row_strip_count:
            pass
        elif curr_row_total == per_row_strip_count:
            curr_row_total = 0
            curr_row_num += 1
        else:
            return False

    # Check vertical/col strips
    curr_col_total = 0
    curr_col_num = 0
    for idx, col_count in enumerate(col_counts):
        curr_col_total += col_count
        col_to_ver_cut_map[idx] = curr_col_num

        if curr_col_total < per_col_strip_count:
            pass
        elif curr_col_total == per_col_strip_count:
            curr_col_total = 0
            curr_col_num += 1
        else:
            return False

    print(row_to_hor_cut_map)
    print(col_to_ver_cut_map)

    piece_count = [[0 for _ in range(V+1)] for _ in range(H+1)]
    for ri in range(R):
        for ci in range(C):
            curr_char = choc_chip[ri][ci]

            # print(ri, ci)

            if curr_char == '@':
                piece_count[row_to_hor_cut_map[ri]][col_to_ver_cut_map[ci]] += 1

    for row in piece_count:
        print(row)

    for hi in range(H+1):
        for vi in range(V+1):
            if piece_count[hi][vi] != each_piece_count:
                return False

    return True


for ti in range(int(input())):
    R, C, H, V = list(map(int, input().strip().split()))

    choc_chip = list()
    row_counts = [0 for _ in range(R)]
    col_counts = [0 for _ in range(C)]
    total_chips = 0
    total_pieces = (H + 1) * (V + 1)
    for ri in range(R):
        row_string = input()
        choc_chip.append(row_string)
        curr_row_total = 0
        for idx, ch in enumerate(row_string):
            if row_string[idx] == '@':
                curr_row_total += 1
                col_counts[idx] += 1
                total_chips += 1
        row_counts[ri] = curr_row_total

    for row in choc_chip:
        print(row)
    print(total_chips, total_pieces)

    if total_chips % total_pieces != 0:
        print("Case #{}: IMPOSSIBLE".format(ti + 1))
    else:
        per_row_strip_count = int(total_chips / (H+1))
        per_col_strip_count = int(total_chips / (V+1))
        print(per_row_strip_count, per_col_strip_count)
        each_piece_count = int(total_chips / total_pieces)
        if cut_possible(row_counts, col_counts, per_row_strip_count, per_col_strip_count, choc_chip, R, C, H, V, each_piece_count):
            print("Case #{}: POSSIBLE".format(ti+1))
        else:
            print("Case #{}: IMPOSSIBLE".format(ti + 1))


"""
6
3 6 1 1
.@@..@
.....@
@.@.@@
4 3 1 1
@@@
@.@
@.@
@@@
4 5 1 1
.....
.....
.....
.....
4 4 1 1
..@@
..@@
@@..
@@..
3 4 2 2
@.@@
@@.@
@.@@
3 4 1 2
.@.@
@.@.
.@.@

"""