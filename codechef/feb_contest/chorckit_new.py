import math
import random
from bisect import bisect

random.seed(0)
# import time

# start_time = time.time()
n, m, a, x, r = list(map(int, input().split()))
s = input()

# pretty melodies and their values
t = list()
c = list()

for _ in range(m):
    inp = input()
    t1, c1 = inp.strip().split()
    t.append(t1)
    c.append(int(c1))

# good melodies and their costs
p = list()
q = list()

for _ in range(a):
    inp = input()
    p1, q1 = inp.strip().split()
    p.append(p1)
    q.append(int(q1))


def char_value(c):
    ord_val = ord(c)
    if ord_val <= 90:
        return ord_val - 38
    else:
        return ord_val - 96


# Pre-processing work
pretty_values = dict(zip(t, c))
good_costs = dict(zip(p, q))
good_melody_indices = dict(zip(p, list(range(1, len(p) + 1))))

pretty_values_per_length = dict()
for pretty_melody in pretty_values:
    pretty_values_per_length[pretty_melody] = float(pretty_values[pretty_melody]) / float(len(pretty_melody))
sorted_pretty_values_per_length = sorted(pretty_values_per_length.items(), key=lambda x: x[1], reverse=True)
# print(sorted_pretty_values_per_length)


def op_one(orig_str, idx, char):
    return ''.join([orig_str[:idx], char, orig_str[idx+1:]])


def op_two(orig_str, l, r, good_idx):
    return ''.join([orig_str[:l], p[good_idx], orig_str[r+1:]])


def op_three(orig_str, l, r):
    return ''.join([orig_str[:r+1], orig_str[l:r+1], orig_str[r+1:]])


def get_mismatch_pieces(string, pretty_string):
    mismatch_indices = list()
    for idx in range(len(string)):
        if string[idx] != pretty_string[idx]:
            mismatch_indices.append(idx)

    if len(mismatch_indices) == 0:
        return []

    start_points = [mismatch_indices[0]]
    ending_points = list()

    for i in range(1, len(mismatch_indices)):
        elem = mismatch_indices[i]
        if mismatch_indices[i] - mismatch_indices[i-1] > 1:
            start_points.append(elem)
            ending_points.append(mismatch_indices[i-1])
    ending_points.append(mismatch_indices[-1])

    mismatch_pieces = [[s, e] for s, e in zip(start_points, ending_points)]
    return mismatch_pieces


def direct_replacement_cost(curr_idx, string, pretty_string):
    cost = 0
    ops = list()
    for idx, (s_ch, ps_ch) in enumerate(zip(string, pretty_string)):
        if s_ch != ps_ch:
            cost += int(math.fabs(char_value(s_ch) - char_value(ps_ch)))
            ops.append('1 {} {}'.format(curr_idx + idx + 1, ps_ch))

    return cost, ops


def convert_to_pretty(curr_idx, string, pretty_string):
    """
    Returns:
        int: Cost to convert the string to pretty string
        list: list of operations to convert the string to pretty_string
    """
    if len(string) != len(pretty_string):
        return -1, []

    cost = 0
    ops = list()
    # Naive way - replace individual characters
    # for idx, (s_ch, ps_ch) in enumerate(zip(string, pretty_string)):
    #     if s_ch != ps_ch:
    #         cost += int(math.fabs(char_value(s_ch) - char_value(ps_ch)))
    #         ops.append('1 {} {}'.format(curr_idx + idx + 1, ps_ch))

    # Better way - find a cheaper replacement from good strings
    mismatch_pieces = get_mismatch_pieces(string, pretty_string)
    if len(mismatch_pieces):
        for mismatch_piece in mismatch_pieces:
            mm_start = mismatch_piece[0]
            mm_end = mismatch_piece[1]

            curr_cost, curr_ops = direct_replacement_cost(curr_idx + mm_start, string[mm_start: mm_end + 1],
                                                          pretty_string[mm_start: mm_end + 1])

            for j in range(0, mm_start + 1):
                curr_pretty = pretty_string[mm_start - j: mm_end + 1]
                if curr_pretty in good_costs:
                    # check if we can change via good string with better cost
                    curr_pretty_cost = good_costs[curr_pretty]
                    if curr_pretty_cost < curr_cost:
                        curr_cost = curr_pretty_cost
                        curr_ops = ['2 {} {} {}'.format(curr_idx + mm_start - j + 1, curr_idx + mm_end + 1,
                                                        good_melody_indices[curr_pretty])]

            cost += curr_cost
            ops.extend(curr_ops)

    return cost, ops


def get_probability_distribution(numbers):
    sum_all = float(sum(numbers))
    return [float(x) / sum_all for x in numbers]


def get_operations(orig_str, curr_idx, remaining_cost):
    """
    Returns:
        list: Current list of operations
        int: Cost of current list of operations
        int: New starting pointer
        str: New original string
    """
    ops = list()
    cost = None
    next_idx = curr_idx
    new_str = orig_str
    best_value = None


    for pretty_melody, pretty_value_per_length in sorted_pretty_values_per_length:
        curr_pretty_value = pretty_values[pretty_melody]
        if curr_pretty_value > 0:
            curr_cost, curr_ops = convert_to_pretty(curr_idx, orig_str[curr_idx: curr_idx + len(pretty_melody)],
                                                    pretty_melody)
            curr_value = curr_pretty_value - (5 * curr_cost)

            if curr_cost >= 0 and curr_cost <= remaining_cost:
                if best_value is None: # or best_value < curr_value:
                    best_value = curr_value
                    cost = curr_cost
                    ops = curr_ops
                    next_idx = curr_idx + len(pretty_melody)
                    new_str = ''.join([orig_str[:curr_idx], pretty_melody, orig_str[curr_idx + len(pretty_melody):]])
                    break

    # for pretty_melody in pretty_values:
    #     curr_pretty_value = pretty_values[pretty_melody]
    #     if curr_pretty_value > 0:
    #         curr_cost, curr_ops = convert_to_pretty(curr_idx, orig_str[curr_idx: curr_idx + len(pretty_melody)], pretty_melody)
    #         curr_value = curr_pretty_value - (5 * curr_cost)
    #
    #         if curr_cost >= 0:
    #             if best_value is None or best_value < curr_value:
    #                 best_value = curr_value
    #                 cost = curr_cost
    #                 ops = curr_ops
    #                 next_idx = curr_idx + len(pretty_melody)
    #                 new_str = ''.join([orig_str[:curr_idx], pretty_melody, orig_str[curr_idx + len(pretty_melody):]])

    return ops, cost, next_idx, new_str


operations = list()
total_cost = 0
orig_str = s
num_operations = 0
operation_possible = True
curr_idx = 0
# curr_time = time.time()
while total_cost < x and num_operations < 10**5 and operation_possible:# and (curr_time - start_time <= 4.5):
    remaining_cost = x - total_cost
    current_operations, curr_cost, curr_idx, new_str = get_operations(orig_str, curr_idx, remaining_cost)
    # print(current_operations, curr_cost)
    # print(new_str)
    # print(curr_idx)
    # print('\n')

    if curr_cost is None:
        # print("String after operations: '{}'".format(orig_str))
        operation_possible = False
    elif (total_cost + r <= x) and (total_cost + curr_cost + r > x) and (2 * len(orig_str) <= 10**6):
        operation_possible = False
        operations.append('3 1 {}'.format(len(orig_str)))
        # orig_str = op_three(orig_str, 0, len(orig_str) - 1)
        # print("String after operations: '{}'".format(orig_str))
    elif num_operations + len(current_operations) <= 10 ** 5 and total_cost + curr_cost <= x:
        operations.extend(current_operations)
        total_cost += curr_cost
        orig_str = new_str
        num_operations += len(current_operations)
    else:
        # print("String after operations: '{}'".format(orig_str))
        operation_possible = False

    # curr_time = time.time()


print(len(operations))
for operation in operations:
    print(operation)


"""
6 3 2 13 3
AFBBet
BBc 6
cp 4
A 3
EE 3
Bc 1

"""
