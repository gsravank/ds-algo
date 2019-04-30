class Solution:
    def get_next(self, i, j, low, high):
        if i == low:
            return j, high
        elif j == high:
            return high, high - (i - low)
        elif i == high:
            return j, low
        else:
            return low, low + (high - i)

    def helper(self, matrix, low, high):
        if low >= high:
            return

        for curr_col in range(low, high):
            curr_row = low
            old_elem = matrix[low][curr_col]
            for _ in range(4):
                next_row, next_col = self.get_next(curr_row, curr_col, low, high)
                next_elem = matrix[next_row][next_col]

                matrix[next_row][next_col] = old_elem
                old_elem = next_elem
                curr_row, curr_col = next_row, next_col

        self.helper(matrix, low + 1, high - 1)

    def rotate(self, matrix):  # List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        self.helper(matrix, 0, n - 1)


matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
sol.rotate(matrix)

for x in matrix:
    print(x)


# sol = Solution()

# print(sol.get_next(2,0,0,2))