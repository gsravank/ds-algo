import string
import re

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


"""
6 3 2 13 3
AFBBet
BBc 6
cp 4
A 3
EE 3
Bc 1

"""


# define operations
def op_one(orig_str, idx, new_char):
    return ''.join([orig_str[:idx], new_char, orig_str[idx+1:]])


def op_two(orig_str, l, r, good_idx):
    return ''.join([orig_str[:l], p[good_idx], orig_str[r+1:]])


def op_three(orig_str, l, r):
    return ''.join([orig_str[:r+1], orig_str[l:r+1], orig_str[r+1:]])


# character values
all_chars = string.ascii_lowercase + string.ascii_uppercase


def char_value(c):
    ord_val = ord(c)
    if ord_val <= 90:
        return ord_val - 38
    else:
        return ord_val - 96


# if r <= x:
#     print(1)
#     print('{} {} {}'.format(3, 1, n))
# else:
#     print(0)

# Pre-processing work
pretty_values = dict(zip(t, c))
good_costs = dict(zip(p, q))

# Get locations of original string that we shouldn't touch
# orig_melodies = dict()
# for pretty_melody in pretty_values:
#     if


# Function to get the next operation
def get_operation(orig_str, curr_cost, max_cost):
    """
    Takes the original string, cost details and returns an operation to perform

    Returns:
        str: Modified string
        str: Operation in the specified format
        int: New total cost
        bool: Operation possible or not
    """

    return 1, 1, 1


operations = list()
total_cost = 0
orig_str = s
num_operations = 0
operation_possible = True
while total_cost < x and num_operations < 10**5 and operation_possible:
    orig_str, operation, total_cost, operation_possible = get_operation(orig_str, total_cost, x)

    if operation_possible:
        num_operations += 1
        operations.append(operation)


print(len(operations))
for operation in operations:
    print(operation)
