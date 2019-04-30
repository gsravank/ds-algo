from collections import defaultdict


n, m = list(map(int, input().split()))


class Graph:
    def __init__(self):
        self.graph = defaultdict(lambda: list())

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # A function used by DFS
    def DFSUtil(self, v, visited, edge_dir_map, vert_dir_map, in_flag, pos):
        # Mark the current node as visited and print it
        visited[v] = True
        vert_dir_map[v] = in_flag

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                if in_flag:
                    edge_dir_map['#'.join([str(i+1), str(v+1)])] = True
                else:
                    edge_dir_map['#'.join([str(v+1), str(i+1)])] = True
                self.DFSUtil(i, visited, edge_dir_map, vert_dir_map, not in_flag, pos)
            else:
                if vert_dir_map[i] == in_flag:
                    pos[0] = False
                else:
                    if in_flag:
                        edge_dir_map['#'.join([str(i + 1), str(v + 1)])] = True
                    else:
                        edge_dir_map['#'.join([str(v + 1), str(i + 1)])] = True


    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self):
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        edge_dir_map = dict()
        vert_dir_map = dict()
        in_flag = True
        pos = [True]

        # Call the recursive helper function to print
        # DFS traversal
        vert_dir_map[0] = in_flag
        self.DFSUtil(0, visited, edge_dir_map, vert_dir_map, in_flag, pos)

        return pos[0], edge_dir_map


g = Graph()
edges = list()
for _ in range(m):
    ui, vi = list(map(int, input().split()))
    g.addEdge(ui-1, vi-1)
    edges.append('#'.join([str(ui), str(vi)]))

# print(edges)
# print(g.graph)
pos, edge_dir_map = g.DFS()
# print(edge_dir_map)

if pos:
    final_ans = list()
    for edge in edges:
        if edge in edge_dir_map:
            final_ans.append('0')
        else:
            final_ans.append('1')

    print("YES")
    print(''.join(final_ans))
else:
    print("NO")
