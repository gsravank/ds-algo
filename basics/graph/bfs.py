from collections import defaultdict, deque


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

    def BFS(self, start):
        visited = set()
        queue = deque() # appendleft and pop
        bfs = list()

        queue.appendleft(start)
        visited = visited.union([start])  # adding to queue represents visiting that vertex
        bfs.append(str(start))  # add vertex to bfs list on visiting it!

        while len(queue):
            print('Queue: {}'.format(queue))
            print('Visited: {}'.format(visited))
            print('\n')
            # dequeue vertex
            curr_vertex = queue.pop()

            # get its neighbors
            curr_vertex_neighbors = self.graph[curr_vertex]

            # Add non-visited neighbors to queue, mark them as visited
            for neighbor in curr_vertex_neighbors:
                if neighbor not in visited:
                    queue.appendleft(neighbor)

                    visited = visited.union([neighbor])
                    bfs.append(str(neighbor))

        print('BFS: {}'.format('->'.join(bfs)))


g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 5)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.addEdge(5, 6)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)