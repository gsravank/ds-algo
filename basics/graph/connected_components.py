from collections import defaultdict


class UndirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = defaultdict(lambda : list())

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)
        # self.adj_list[v2].append(v1)

    def DFS(self, start, visited):
        visited[start] = True

        for neighbor in self.adj_list[start]:
            if not visited[neighbor]:
                self.DFS(neighbor, visited)

    def connected_components(self):
        visited = [False] * self.num_vertices

        num_connected_components = 0
        for start in range(self.num_vertices):
            if not visited[start]:
                num_connected_components += 1
                self.DFS(start, visited)

        return num_connected_components


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
        # create graph
        print("Creating graph")
        g = UndirectedGraph(self.num_islands)

        print("Adding edges to graph based on given island")
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == 1:
                    curr_cell = self.get_cell_num(i, j)

                    neighbor_i_j, neighbor_cells = self.get_neighbor_cell_nums(i, j)

                    for i_j, cell_num in zip(neighbor_i_j, neighbor_cells):
                        if self.matrix[i_j[0]][i_j[1]]:
                            g.add_edge(curr_cell, cell_num)

        # print("Adjacency Lists for each vertex look like")
        # for i in range(0, self.rows * self.cols):
        #     print(g.adj_list[i])

        # count number of strongly connected components
        num_connected_components = g.connected_components()
        return num_connected_components


graph = [[1, 1, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 0],
         [1, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 1]
         ]

row = len(graph)
col = len(graph[0])

g = Islands(row, col, graph)
print("Number of distinct connected islands is: {}".format(g.count_islands()))