from collections import defaultdict


# This class represents an undirected graph
# using adjacency list representation
class Graph:
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, start):
        stack = list()
        dfs = list()
        visited = set()

        stack.append(start)

        while len(stack):
            print("Stack: {}".format(stack))
            print("Visited: {}".format(visited))
            print('\n')

            curr_vertex = stack.pop()  # popping from stack represents visiting that node

            if curr_vertex not in visited:  # vertex could be in stack twice, so do this check!
                visited = visited.union([curr_vertex])
                dfs.append(str(curr_vertex))  # add vertex to final DFS list on visiting it

                curr_vertex_neighbors = self.graph[curr_vertex]
                for neighbor in curr_vertex_neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)

        print("DFS: {}".format('->'.join(dfs)))


# g = Graph()
# g.addEdge(1, 2)
# g.addEdge(1, 3)
# g.addEdge(2, 4)
# g.addEdge(2, 5)
# g.addEdge(3, 5)
# g.addEdge(4, 5)
# g.addEdge(4, 6)
# g.addEdge(5, 6)
#
# print("Following is Depth First Traversal"
#       " (starting from vertex 2)")
# g.DFS(2)

g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)

print("Following is Depth First Traversal"
      " (starting from vertex 1)")
g.DFS(1)