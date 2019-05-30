def number_of_moves(r, c, matrix):
    row_not_occupied = [1 for _ in range(r)]
    col_not_occupied = [1 for _ in range(c)]

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == '#':
                row_not_occupied[i] = 0
                col_not_occupied[j] = 0

    num_rows = sum(row_not_occupied)
    num_cols = sum(col_not_occupied)

    print(num_rows)
    print(num_cols)

    return


for ti in range(int(input())):
    r, c = list(map(int, input().strip().split()))

    matrix = list()
    for _ in range(r):
        matrix.append(input())

    print("Case #{}: {}".format(ti + 1, number_of_moves(r, c, matrix)))

"""
5
2 2
..
.#
4 4
.#..
..#.
#...
...#
3 4
#.##
....
#.##
1 1
.
1 2
##

"""