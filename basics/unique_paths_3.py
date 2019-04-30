class Solution:
    def helper(self, i, j, end_i, end_j, count, grid, m, n):
        # print(i, j)
        if i < 0 or j < 0 or i >= m or j >= n:
            return 0

        if grid[i][j] == -1:
            return 0

        if grid[i][j] == 2:
            if count == 0:
                return 1
            else:
                return 0

        if count == 0:
            if i == end_i and j == end_j:
                # dp[i][j] = 1
                # print('\n--\n')
                return 1
            else:
                return 0



        temp = grid[i][j]
        grid[i][j] = -1

        # for x in grid:
        #     print(x)
        # print('\n\n')

        total = 0
        total += self.helper(i, j + 1, end_i, end_j, count - 1, grid, m, n)
        total += self.helper(i, j - 1, end_i, end_j, count - 1, grid, m, n)
        total += self.helper(i + 1, j, end_i, end_j, count - 1, grid, m, n)
        total += self.helper(i - 1, j, end_i, end_j, count - 1, grid, m, n)

        grid[i][j] = temp
        # dp[i][j] = total

        return total

    def uniquePathsIII(self, grid):# List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_i = i
                    start_j = j
                elif grid[i][j] == 2:
                    end_i = i
                    end_j = j
                elif grid[i][j] == 0:
                    count += 1

        # for x in grid:
        #     print(x)
        # print('\n\n')
        # print(count)
        # print(start_i, start_j)
        # print(end_i, end_j)
        # print('\n\n')

        a = self.helper(start_i, start_j, end_i, end_j, count + 1, grid, m, n)

        # for x in dp:
        #     print(x)

        return a
        # return dp[start_i][start_j]


grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# grid = [[1, 2]]
sol = Solution()

print(sol.uniquePathsIII(grid))