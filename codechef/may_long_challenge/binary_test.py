import random


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

    print(waits[::-1])
    print(zero_positions[::-1])

    final_state = [1 for _ in range(n)]
    num_zeros = len(waits)
    for zero_idx in range(num_zeros - 1, -1, -1):
        curr_zero_pos = zero_positions[zero_idx]
        curr_zero_wait = waits[zero_idx]

        curr_zero_final_pos = get_final_position(curr_zero_pos, curr_zero_wait, zero_idx, z, n)
        final_state[curr_zero_final_pos] = 0

    return final_state


def get_random_binary(length):
    s = [0 for _ in range(length)]

    for i in range(length):
        if random.random() >= 0.5:
            s[i] = 1

    return s


def make_move(state):
    curr_idx = 0
    length = len(state)

    while curr_idx < length - 1:
        if state[curr_idx] == 0 and state[curr_idx + 1] == 1:
            state[curr_idx] = 1
            state[curr_idx + 1] = 0
            curr_idx += 2
        else:
            curr_idx += 1

    return state


def play_game(length, num_moves, state):
    curr_moves = 0
    done = False
    while curr_moves < num_moves and not done:
        next_state = make_move(state[:])
        curr_moves += 1

        if next_state == state:
            done = True
        else:
            state = next_state

        print("After {} moves: {}".format(curr_moves, state))

    return state


length = 15
num_moves = 5

# state = get_random_binary(length)
state = [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
print("Initial State: {}\n".format(state))

fs1 = play_game(length, num_moves, state)
print("\nFinal State:   {}\n\n".format(fs1))
fs2 = get_final_state(length, num_moves, state)
print("Final Guess: {}".format(fs2))

print(fs1 == fs2)