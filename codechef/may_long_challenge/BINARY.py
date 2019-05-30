def plus(x):
    return max(x, 0)


def get_final_position(start_pos, total_wait, num_zeros_to_right, num_moves, n):
    max_position = n - 1 - num_zeros_to_right

    return min(max_position, start_pos + num_moves - total_wait)


def get_final_state(n, z, a):
    waits = list()
    zero_positions = list()
    dist = 0
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            zero_positions.append(i)
            if len(waits) == 0:
                waits.append(0)
            else:
                waits.append(plus(waits[-1] - dist + 1))

            dist = 0
        else:
            dist += 1

    final_state = [1 for _ in range(n)]
    num_zeros = len(waits)
    for zero_idx in range(num_zeros - 1, -1, -1):
        curr_zero_pos = zero_positions[zero_idx]
        curr_zero_wait = waits[zero_idx]

        curr_zero_final_pos = get_final_position(curr_zero_pos, curr_zero_wait, zero_idx, z, n)
        final_state[curr_zero_final_pos] = 0

    return final_state


for _ in range(int(input())):
    n, z = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))

    final_state = get_final_state(n, z, a)

    for x in final_state:
        print(x, end=' ')
    print()





"""
2
6 2
0 1 1 0 1 1
4 4
0 1 0 1

"""

"""
6
14 5
1 1 1 0 0 1 0 0 0 1 1 1 1 1
14 6
1 1 1 0 0 1 0 0 0 1 1 1 1 1
14 7
1 1 1 0 0 1 0 0 0 1 1 1 1 1
14 8
1 1 1 0 0 1 0 0 0 1 1 1 1 1
14 9
1 1 1 0 0 1 0 0 0 1 1 1 1 1
14 10
1 1 1 0 0 1 0 0 0 1 1 1 1 1

"""