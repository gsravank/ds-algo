class DisjointSet:
    def __init__(self, num_items):
        self.num_items = num_items
        self.parent = list(range(num_items))
        self.rank = [0] * num_items

    def union(self, i, j):
        parent_i = self.find(i)
        parent_j = self.find(j)

        rank_i = self.rank[parent_i]
        rank_j = self.rank[parent_j]

        if rank_i < rank_j:
            # place tree of i under parent of j
            self.parent[parent_i] = parent_j
        elif rank_j < rank_i:
            # place tree of j under parent of i
            self.parent[parent_j] = parent_i
        else:
            # pick any and place under the parent of other
            # increment rank of the one you placed under
            self.parent[parent_j] = parent_i
            self.rank[parent_i] += 1

        if parent_i != parent_j:
            self.parent[j] = parent_i

    def find(self, i):
        if i == self.parent[i]:
            return i
        else:
            result = self.find(self.parent[i])
            self.parent[i] = result
            return result


class Islands:
    def __init__(self, m, n, matrix):
        self.rows = m
        self.cols = n
        self.matrix = matrix
        self.all_cell_numbers, self.num_islands = self.get_all_cell_numbers()

    def get_all_cell_numbers(self):
        all_cell_numbers = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]
        curr_cell = 0

        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j]:
                    all_cell_numbers[i][j] = curr_cell
                    curr_cell += 1

        return all_cell_numbers, curr_cell

    def get_cell_num(self, row, col):
        return self.all_cell_numbers[row][col]

    def get_neighbor_cell_nums(self, row, col):
        rdiffs = [0, 0, 1, -1, 1, 1, -1, -1]
        cdiffs = [1, -1, 0, 0, 1, -1, 1, -1]

        neighbors = list()
        for rd, cd in zip(rdiffs, cdiffs):
            if ( -1 < row+rd < self.rows ) and ( -1 < col+cd < self.cols ):
                neighbors.append((row+rd, col+cd))

        neighbor_cell_nums = [self.get_cell_num(x[0], x[1]) for x in neighbors]
        return neighbors, neighbor_cell_nums

    def count_islands(self):
        print("Creating a disjoint set, with each island as its own set")
        dsj_set = DisjointSet(self.num_islands)

        print("Union two islands if they are neighbors")
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == 1:
                    curr_cell = self.get_cell_num(i, j)

                    neighbor_i_j, neighbor_cells = self.get_neighbor_cell_nums(i, j)

                    for i_j, cell_num in zip(neighbor_i_j, neighbor_cells):
                        if self.matrix[i_j[0]][i_j[1]]:
                             dsj_set.union(curr_cell, cell_num)

        print("Parent list for disjoint set looks like: ", end='')
        print(dsj_set.parent)

        print("Counting number of connected components based on different sets in disjoint set")
        return len(set(dsj_set.parent))


graph = [[1, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 0],
         [1, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0, 1]
         ]

row = len(graph)
col = len(graph[0])

i = Islands(row, col, graph)
print("Number of islands is: {}".format(i.count_islands()))