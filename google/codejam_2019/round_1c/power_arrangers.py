from collections import defaultdict, Counter

all_chars = set(['A', 'B', 'C', 'D', 'E'])
# all_chars = set(['A', 'B', 'C'])


def identify_missing_char(identified_chars, curr_position_chars):
    remaining_chars = all_chars - set(identified_chars)

    if len(remaining_chars) == 1:
        return list(remaining_chars)[0]

    curr_pos_chars_counts = dict()
    for remaining_char in remaining_chars:
        curr_pos_chars_counts[remaining_char] = 0

    for curr_position_char in curr_position_chars:
        curr_pos_chars_counts[curr_position_char] += 1

    min_count = len(curr_position_chars) + 1
    min_char = None
    for char, count in curr_pos_chars_counts.items():
        if count < min_count:
            min_count = count
            min_char = char

    return min_char


def get_position_num(perm_num, perm_pos):
    return (5 * perm_num) + perm_pos


def play_game():
    useful_perms = list(range(119))
    curr_position = 0
    identified_chars = list()

    while curr_position < 5:
        # Save perm numbers of chars at this position
        char_positions_dict = defaultdict(lambda: list())

        # Get all chars at curr_position from all useful_perms
        curr_position_chars = list()
        for useful_perm in useful_perms:
            print(get_position_num(useful_perm, curr_position) + 1, flush=True)
            input_char = input()

            curr_position_chars.append(input_char)
            char_positions_dict[input_char].append(useful_perm)

        # Find the missing char based on whatever we already identified and what we saw in this current position
        curr_identified_char = identify_missing_char(identified_chars, curr_position_chars)

        identified_chars.append(curr_identified_char)
        useful_perms = char_positions_dict[curr_identified_char][:]
        curr_position += 1

    print(''.join(identified_chars), flush=True)
    success_flag = input()

    return


t, f = list(map(int, input().strip().split()))

for ti in range(t):
    play_game()

