from collections import Counter

n, m = list(map(int, input().strip().split()))

u = list()
v = list()
# degrees = dict()
edges = list()
max_deg = 0
max_deg_vert = None
# vertex_edges = dict()
edge_vertices = list()

for _ in range(m):
    ui, vi = list(map(int, input().strip().split()))
    u.append(ui)
    v.append(vi)
    edges.append((ui, vi))

    edge_vertices.append(ui)
    edge_vertices.append(vi)
    #
    # if ui in degrees:
    #     degrees[ui] += 1
    # else:
    #     degrees[ui] = 1
    #
    # if vi in degrees:
    #     degrees[vi] += 1
    # else:
    #     degrees[vi] = 1

    # if ui in vertex_edges:
    #     vertex_edges[ui].append((ui, vi))
    # else:
    #     vertex_edges[ui] = [(ui, vi)]
    #
    # if vi in vertex_edges:
    #     vertex_edges[vi].append((ui, vi))
    # else:
    #     vertex_edges[vi] = [(ui, vi)]

degrees = Counter(edge_vertices)
for vertex in degrees:
    if degrees[vertex] > max_deg:
        max_deg = degrees[vertex]
        max_deg_vert = vertex


# Kruskal's algo but first pick edges coming out of max_deg_vert
other_edges = list()
vertices_covered = set([])
for edge in edges:
    if edge[0] == max_deg_vert or edge[1] == max_deg_vert:
        print("{} {}".format(edge[0], edge[1]))
        vertices_covered = vertices_covered.union(set([edge[0], edge[1]]))
    else:
        other_edges.append(edge)

for other_edge in other_edges:
    if other_edge[0] in vertices_covered and other_edge[1] in vertices_covered:
        pass
    else:
        vertices_covered = vertices_covered.union(set([other_edge[0], other_edge[1]]))
        print("{} {}".format(other_edge[0], other_edge[1]))

    if len(vertices_covered) == n:
        break