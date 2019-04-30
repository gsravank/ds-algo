from collections import defaultdict


def is_cycle_aux(vertex, adj_list, visited, parent):
    # modified DFS to check if cycle exists
    visited[vertex] = True

    for neighbor in adj_list[vertex]:
        if not visited[neighbor]:
            if is_cycle_aux(neighbor, adj_list, visited, vertex):
                return True
        elif neighbor != parent:
            return True

    return False


def isCyclic(vertices, adj_list):
    visited = [False] * vertices
    parent = -1

    for vertex in range(vertices):
        if not visited[vertex]:
            if is_cycle_aux(vertex, adj_list, visited, parent):
                return 1
    return 0


for _ in range(int(input())):
    v, e = list(map(int, input().split()))

    vertices = v
    adj = defaultdict(lambda : list())
    edges = list(map(int, input().split()))
    for e_num in range(e):
        u = edges[e_num * 2]
        v = edges[(e_num * 2) + 1]
        adj[u].append(v)
        if u != v:
            adj[v].append(u)

    # print(adj)
    print(isCyclic(vertices, adj))



"""
2
2 2
0 1 0 0
4 3
0 1 1 2 2 3

1
6 8
0 1 0 4 0 3 1 2 3 4 4 2 5 4 5 2

1
6 8
0 1 0 4 0 3 1 2 3 4 4 2 5 4 2 5

"""