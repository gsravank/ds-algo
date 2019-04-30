from collections import defaultdict


def derangement(a, n):
    color_idx_dict = defaultdict(lambda: list())
    color_counts = defaultdict(lambda: 0)
    final_color_idx_dict = defaultdict(lambda: list())
    idx_color_dict = dict()

    for idx, ai in enumerate(a):
        color_idx_dict[ai].append(idx + 1)
        color_counts[ai] += 1
        idx_color_dict[idx + 1] = ai

    # init check
    for color in color_idx_dict:
        rem_count = n - color_counts[color]

        if rem_count < color_counts[color]:
            return "No", []

    if len(color_idx_dict) == 1:
        return "No", []

    sorted_colors = sorted(color_counts, key=color_counts.get, reverse=True)
    lying_around = defaultdict(lambda: list())

    for j, curr_color in enumerate(sorted_colors):
        num_other_cols_to_pick = color_counts[curr_color]
        lying_around[curr_color] = color_idx_dict[curr_color]
        color_idx_dict[curr_color] = list()

        # Get other color idxs from lower counts
        for remaining_color in sorted_colors[j+1:]:
            if num_other_cols_to_pick == 0:
                break
            else:
                num_remaining_color = len(color_idx_dict[remaining_color])

                if num_remaining_color >= num_other_cols_to_pick:
                    final_color_idx_dict[curr_color].extend(color_idx_dict[remaining_color][:num_other_cols_to_pick])
                    color_idx_dict[remaining_color] = color_idx_dict[remaining_color][num_other_cols_to_pick:]

                    num_other_cols_to_pick = 0
                else:
                    final_color_idx_dict[curr_color].extend(color_idx_dict[remaining_color])
                    color_idx_dict[remaining_color] = list()

                    num_other_cols_to_pick -= num_remaining_color

        # Get other color idxs from lying around
        if num_other_cols_to_pick > 0:
            for lying_color in lying_around:
                if lying_color != curr_color:
                    if num_other_cols_to_pick == 0:
                        break

                    lying_color_av = len(lying_around[lying_color])

                    if lying_color_av >= num_other_cols_to_pick:
                        final_color_idx_dict[curr_color].extend(lying_around[lying_color][:num_other_cols_to_pick])
                        lying_around[lying_color] = lying_around[lying_color][num_other_cols_to_pick:]

                        num_other_cols_to_pick = 0
                    else:
                        final_color_idx_dict[curr_color].extend(lying_around[lying_color])
                        lying_around[lying_color] = list()

        if num_other_cols_to_pick > 0:
            return "No", []

    # print(final_color_idx_dict)
    final_der = list()
    for idx, ai in enumerate(a):
        other_idx = final_color_idx_dict[ai].pop()
        final_der.append(idx_color_dict[other_idx])
    # print(final_der)

    return "Yes", final_der


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    pos_string, pos_der = derangement(a, n)
    if pos_string == "Yes":
        print(pos_string)
        for item in pos_der:
            print(item, end=' ')
        print()
    else:
        print(pos_string)


"""
2
9
1 1 1 2 2 2 3 3 3
2
1 1

1
9
1 1 1 2 2 2 3 3 3

1
14
1 1 2 2 2 3 3 3 3 4 4 4 4 4

"""