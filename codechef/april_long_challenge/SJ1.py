from collections import defaultdict
import math


gcd_map = dict()


def get_gcd(a, b):
    if a in gcd_map:
        if b in gcd_map[a]:
            return gcd_map[a][b]

    curr_gcd = int(math.gcd(a, b))
    if a in gcd_map:
        gcd_map[a][b] = curr_gcd
    else:
        gcd_map[a] = dict()
        gcd_map[a][b] = curr_gcd

    if b in gcd_map:
        gcd_map[b][a] = curr_gcd
    else:
        gcd_map[b] = dict()
        gcd_map[b][a] = curr_gcd

    return curr_gcd


class Graph:
    def __init__(self):
        self.graph = defaultdict(lambda: list())

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, vs):
        m = len(self.graph)

        leaves = dict()
        root_to_node_path_gcd = [0 for _ in range(m)]
        root_to_node_path_gcd[0] = vs[0]

        stack = list()
        visited = [False for _ in range(m)]
        visited[0] = True
        stack.append(0)

        while len(stack):
            top_vertex = stack[-1]

            neighbor = None
            for i in self.graph[top_vertex]:
                if not visited[i]:
                    neighbor = i
                    break

            if neighbor is not None:
                visited[neighbor] = True
                stack.append(neighbor)

                root_to_node_path_gcd[neighbor] = math.gcd(root_to_node_path_gcd[top_vertex], vs[neighbor])
            else:
                if len(self.graph[top_vertex]) == 1 and top_vertex != 0:
                    leaves[top_vertex] = True

                stack.pop()

        return leaves, root_to_node_path_gcd


for _ in range(int(input())):
    n = int(input())
    g = Graph()

    for _ in range(n-1):
        ui, vi = list(map(int, input().split()))
        g.add_edge(ui-1, vi-1)

    vs = list(map(int, input().split()))
    ms = list(map(int, input().split()))

    leaves, root_to_node_path_gcd = g.DFS(vs)
    # print("Leaves: {}".format(leaves.keys()))
    # print("Root to node path GCD: {}".format(root_to_node_path_gcd))

    for idx, curr_gcd in enumerate(root_to_node_path_gcd):
        if idx in leaves:
            print(ms[idx] - math.gcd(ms[idx], curr_gcd), end=' ')


"""
1
5
1 2
2 5
1 3
3 4
2 3 4 6 7
1 2 3 2 10

"""