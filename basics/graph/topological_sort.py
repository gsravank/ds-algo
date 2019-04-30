from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(lambda : list())
        self.vertices = set()

    def add_edge(self, vert1, vert2):
        self.graph[vert1].append(vert2)
        self.vertices = self.vertices.union([vert1, vert2])

    def get_unvisited(self, neighbors, visited):
        for neighbor in neighbors:
            if neighbor not in visited:
                return neighbor
        return None

    def topological_sort_util(self, vert, topo_stack, visited):
        stack = list()
        visited = visited.union([vert])
        stack.append(vert)

        while len(stack):
            # peek top of stack
            curr_node = stack[-1]

            # get unvisited neighbor of stack
            unvisited = self.get_unvisited(self.graph[curr_node], visited)

            if unvisited is not None:
                # if present, mark this neigbbor as visited and add to top of stack
                visited = visited.union([unvisited])
                stack.append(unvisited)
            else:
                # else no unvisited neighbor present, then pop elem from top of stack
                # add this popped element into topo_stack
                stack.pop()
                topo_stack.append(curr_node)

        return visited, topo_stack

    def topological_sort(self):
        visited = set()
        topo_stack = list()

        for vert in sorted(list(self.vertices)):
            if vert not in visited:
                visited, topo_stack = self.topological_sort_util(vert, topo_stack, visited)

        print("Topological sort: {}".format('->'.join(topo_stack[::-1])))


g = Graph()
edge_dict = {'m': ['q', 'r', 'x'], 'n': ['o', 'u', 'q'], 'o': ['r', 's', 'v'], 'p': ['o', 's', 'z'],
             'q': ['t'], 'r': ['u', 'y'], 's': ['r'],
             't': [], 'u': ['t'], 'v': ['w', 'x'], 'w': ['z'],
             'x': [], 'y': ['v'], 'z': []}

print("Adding edges to graph")
for start in edge_dict:
    for end in edge_dict[start]:
        g.add_edge(start, end)

print("Calling topological sort")
g.topological_sort()
