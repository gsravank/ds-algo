class UndirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    def hamiltonian_path_util(self, vertex, visited, next, start):
        visited[vertex] = True

        if all(visited) and self.adj_matrix[vertex][start]:
            next[vertex] = start
            return True

        for neighbor, edge_flag in enumerate(self.adj_matrix[vertex]):
            if edge_flag and not visited[neighbor]:
                next[vertex] = neighbor
                if self.hamiltonian_path_util(neighbor, visited, next, start):
                    return True
                next[vertex] = -1

        visited[vertex] = False
        return False

    def hamiltonian_path(self):
        visited = [False] * self.num_vertices
        next = [-1] * self.num_vertices
        start_vertex = 3

        if self.hamiltonian_path_util(start_vertex, visited, next, start_vertex):
            i = start_vertex
            path = list()
            for _ in range(self.num_vertices + 1):
                path.append(i)
                i = next[i]

            print("Hamiltonian Path: {}".format('->'.join([str(x) for x in path])))
            return True
        else:
            print("No hamiltonian path exists for this graph")
            return False


g = UndirectedGraph(5)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 4)

g.hamiltonian_path()
