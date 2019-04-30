class Solution:
    def get_neighbors(self, i, j, m, n):
        diffs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        neighbors = list()
        for x_diff, y_diff in diffs:
            x = i + x_diff
            y = j + y_diff

            if x >= 0 and x < m and y >= 0 and y < n:
                neighbors.append((x, y))

        return neighbors

    def DFS(self, i, j, grid, visited, m, n):
        visited[i][j] = 1

        print(i, j)
        print(self.get_neighbors(i, j, m, n))

        for neighbor_i, neighbor_j in self.get_neighbors(i, j, m, n):
            if not visited[neighbor_i][neighbor_j] and grid[neighbor_i][neighbor_j] == "1":
                self.DFS(neighbor_i, neighbor_j, grid, visited, m, n)

        return

    def numIslands(self, grid):# List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]
        num_islands = 0
        for i in range(m):
            for j in range(n):
                for x in visited:
                    print(x)
                print('\n')
                if not visited[i][j] and grid[i][j] == "1":
                    num_islands += 1
                    self.DFS(i, j, grid, visited, m, n)

        return num_islands


grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
sol = Solution()

print(sol.numIslands(grid))