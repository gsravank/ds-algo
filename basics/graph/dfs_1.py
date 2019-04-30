class Node:
    def __init__(self, idx):
        self.idx = idx
        self.adjacent_nodes = list()
        self.visited = False


def get_unvisited_neighbor(node):
    for neighbor in node.adjacent_nodes:
        if not neighbor.visited:
            return neighbor

    return None


class Graph:
    def __init__(self):
        self.nodes = list()

    def add_edge(self, node1, node2):
        node1.adjacent_nodes.append(node2)
        node2.adjacent_nodes.append(node1)

        self.nodes.extend([node1, node2])
        self.nodes = list(set(self.nodes))

    def DFS(self, start_node):
        stack = list()
        dfs = list()
        start_node.visited = True  # add node to stack when visited
        dfs.append(str(start_node.idx))
        stack.append(start_node)

        while len(stack):
            unvis_nbr = get_unvisited_neighbor(stack[-1])

            if unvis_nbr is not None:
                unvis_nbr.visited = True
                dfs.append(str(unvis_nbr.idx))
                stack.append(unvis_nbr)
            else:
                stack.pop()  # remove node from stack when all neighbors are done

        for node in self.nodes:
            node.visited = False

        print("DFS: {}".format('->'.join(dfs)))


nodes = list()
for i in range(1, 8):
    nodes.append(Node(i))


g = Graph()
g.add_edge(nodes[0], nodes[1])
g.add_edge(nodes[0], nodes[2])
g.add_edge(nodes[1], nodes[3])
g.add_edge(nodes[1], nodes[4])
g.add_edge(nodes[2], nodes[5])
g.add_edge(nodes[2], nodes[6])

print("Following is Depth First Traversal"
      " (starting from vertex 1)")
g.DFS(nodes[0])

print("Following is Depth First Traversal"
      " (starting from vertex 4)")
g.DFS(nodes[3])
