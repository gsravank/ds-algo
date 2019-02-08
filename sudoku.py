import math


class Solution:
    def abs(self, n):
        return int(math.fabs(n))

    def bt_sudoku(self, A, row, col):
        # if col == 3:
        #     input('')
        # print(row, col)
        # for x in A:
        #     print(x)
        # print('\n\n')

        if row == 9:
            return True

        if col == 8:
            next_row = row + 1
            next_col = 0
        else:
            next_row = row
            next_col = col + 1

        if A[row][col] > 0:
            return self.bt_sudoku(A, next_row, next_col)

        not_allowed = set()
        # Get all numbers from the row
        for j in range(9):
            if j != col:
                curr_num = A[row][j]
                if curr_num != 0:
                    if j < col:
                        not_allowed = not_allowed.union([self.abs(curr_num)])
                    else:
                        if curr_num > 0:
                            not_allowed = not_allowed.union([self.abs(curr_num)])

        # Get all numbers from the col
        for j in range(9):
            if j != row:
                curr_num = A[j][col]
                if curr_num != 0:
                    if j < row:
                        not_allowed = not_allowed.union([self.abs(curr_num)])
                    else:
                        if curr_num > 0:
                            not_allowed = not_allowed.union([self.abs(curr_num)])

        # Get all numbers from local 3x3 square
        row_range_min = int(row/3) * 3
        row_range_max = row_range_min + 2

        col_range_min = int(col/3) * 3
        col_range_max = col_range_min + 2

        # print(row_range_min, row_range_max)
        # print(col_range_min, col_range_max)

        for r in range(row_range_min, row_range_max + 1, 1):
            for c in range(col_range_min, col_range_max + 1, 1):
                curr_num = A[r][c]
                if r > row or (c > col and r == row):
                    if curr_num != 0:
                        if curr_num > 0:
                            not_allowed = not_allowed.union([self.abs(curr_num)])
                elif r == row and c == col:
                    pass
                else:
                    if curr_num != 0:
                        not_allowed = not_allowed.union([self.abs(curr_num)])

        allowed = set(list(range(1,10,1))) - not_allowed
        # print(not_allowed)
        # print(allowed)
        # print('\n\n')

        for option in allowed:
            A[row][col] = (-1 * option)
            i = self.bt_sudoku(A, next_row, next_col)

            if i:
                return True

        return False


    # @param A : list of list of chars
    # @return nothing
    def solveSudoku(self, A):
        import math
        N = 9

        for idx in range(9):
            for jdx in range(9):
                if A[idx][jdx] != '.':
                    A[idx][jdx] = int(A[idx][jdx])
                else:
                    A[idx][jdx] = 0

        for x in A:
            print(x)
        print('\n\n')

        row = 0
        col = 0
        found = self.bt_sudoku(A, row, col)

        for idx in range(9):
            for jdx in range(9):
                A[idx][jdx] = str(int(math.fabs(A[idx][jdx])))

        return A

test = [ ["5","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."], ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"], [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"] ]

sol = Solution()
print(sol.solveSudoku(test))