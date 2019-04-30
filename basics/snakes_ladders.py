from collections import defaultdict
import math
from collections import deque


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = defaultdict(lambda: list())

    def add_edge(self, v1, v2):
        self.adj_list[v1].append(v2)

    def min_distance(self, start, end):
        visited = [False] * self.num_vertices
        queue = deque()
        parent = [-1] * self.num_vertices

        queue.appendleft((start, 0))
        visited[start] = True

        while len(queue):
            curr_node_details = queue.pop()
            curr_node = curr_node_details[0]
            curr_node_dist = curr_node_details[1]

            for neighbor in self.adj_list[curr_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    neighbor_dist = curr_node_dist + 1
                    parent[neighbor] = curr_node

                    if neighbor == end:
                        # path = list()
                        # i = end
                        # while i != -1:
                        #     path.append(i)
                        #     i = parent[i]
                        #
                        # print("Path from start to end node: {}".format('->'.join([str(x+1) for x in path[::-1]])))
                        return neighbor_dist

                    queue.appendleft((neighbor, neighbor_dist))

        return -1


class Solution:
    def get_row_col(self, cell_idx, n):
        cell_num = cell_idx + 1
        row_from_bot = int(math.ceil(float(cell_num) / n))

        if row_from_bot % 2 == 1:
            col_from_left = (cell_idx % n) + 1
        else:
            col_from_left = n - (cell_idx % n)

        row_id = n - row_from_bot
        col_id = col_from_left - 1

        return row_id, col_id

    def construct_graph(self, board):
        n = len(board)
        num_vertices = n * n
        g = Graph(num_vertices)

        for curr_cell_idx in range(0, num_vertices):
            # get the next 6 cells
            adj_cells = [x + curr_cell_idx for x in range(1, 7) if (x+curr_cell_idx) < num_vertices]

            # for each adjacent cell
            for adj_cell_idx in adj_cells:
                # get row, col of this cell
                adj_cell_row_col = self.get_row_col(adj_cell_idx, n)

                # check if that cell is snake or ladder
                # if not add the nbr_cell_idx to adj_list of curr_cell_idx
                adj_cell_content = board[adj_cell_row_col[0]][adj_cell_row_col[1]]
                if adj_cell_content == -1:
                    g.add_edge(curr_cell_idx, adj_cell_idx)
                else:
                    # else add the other_cell_idx of the other end of the snake/ladder to adj_list of curr_cell_idx
                    g.add_edge(curr_cell_idx, adj_cell_content - 1)

        return g

    def snakesAndLadders(self, board):  # List[List[int]]) -> int:
        # construct graph based on given board
        n = len(board)
        # print("Constructing graph based on given board")
        g = self.construct_graph(board)

        # print("Adjacency list of all cells look like")
        # for i in range(n*n):
        #     print("cell number = {}, next jumps = {}".format(i+1, ','.join([str(x+1) for x in g.adj_list[i]])))

        # perform BFS starting from node 0 to get shortest path distances from 0
        # return distance of last node (-1 if node is not reachable)
        min_distance = g.min_distance(0, n*n-1)
        return min_distance


sol = Solution()
board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1]
]
print(sol.snakesAndLadders(board))
