import string

t = int(input())

chars = string.ascii_uppercase


def min_operations(s):
    n = len(s)
    if n == 1:
        return 1

    freq_counts = dict()
    for c in chars:
        freq_counts[c] = 0

    for c in s:
        freq_counts[c] += 1

    num_distinct = 0
    for c in freq_counts:
        if freq_counts[c] > 0:
            num_distinct += 1

    sorted_freq = sorted(freq_counts.values())
    # print(sorted_freq)

    min_op = n + 1
    for num_chars in range(1, 27):
        cur_op = 0
        # if num_chars <= num_distinct:
        if n % num_chars == 0:
            char_freq = int(n / num_chars)

            last_i = sorted_freq[-1 * num_chars:]

            for last_freq in last_i:
                if last_freq < char_freq:
                    cur_op += (char_freq - last_freq)

            # print(num_chars)
            # print(char_freq)
            # print(last_i)
            # print(cur_op)
            # print('\n')

            if cur_op < min_op:
                min_op = cur_op
    return min_op


for _ in range(t):
    s = input()
    print(min_operations(s))


"""
ABCDBEFGAH
"""