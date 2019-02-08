import timeit
import matplotlib.pyplot as plt


def format_state(a):
    state = list()
    for each_row in a:
        curr_str_items = []
        for col in each_row:
            if col == 0:
                curr_str_items.append('.')
            else:
                curr_str_items.append('Q')
        state.append(''.join(curr_str_items))
    return state


def safe_position(N, a, curr_row, curr_col):
    # check same column in all previous rows
    for i in range(curr_row):
        if a[i][curr_col] == 1:
            return False

    # check left and right diagonal through (curr_row, curr_col)
    for dist, prev_row in enumerate(range(curr_row - 1, -1, -1)):
        left_col_to_check = curr_col - dist - 1
        right_col_to_check = curr_col + dist + 1

        if left_col_to_check >= 0:
            if a[prev_row][left_col_to_check] == 1:
                return False

        if right_col_to_check <= N - 1:
            if a[prev_row][right_col_to_check] == 1:
                return False

    return True


def get_n_queens(N, a, row, states):
    if row == N:
        states.append(format_state(a))
        return

    for col in range(N):
        if safe_position(N, a, row, col):
            a[row][col] = 1
            get_n_queens(N, a, row+1, states)
            a[row][col] = 0


def nqueens(n):
    a = [[0 for _ in range(n)] for _ in range(n)]
    row = 0
    states = list()

    get_n_queens(n, a, row, states)

    return states


if __name__ == '__main__':
    n = 4
    for x in nqueens(n):
        print(x)
