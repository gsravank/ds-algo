from collections import defaultdict


class Node:
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False
        self.vertices = list()


class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, word, vertex):
        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = int(word[i])

            if index not in root.children:
                root.children[index] = Node()

            root = root.children[index]

        root.vertices.append(vertex)
        root.terminating = True


class Graph:
    def __init__(self, node_values):
        self.graph = defaultdict(lambda: list())
        self.node_values = node_values
        self.subtree_values = defaultdict(lambda : list())
        self.subtree_tries = dict()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def get_subtree_values(self):
        m = len(self.graph)

        stack = list()
        visited = [False for _ in range(m)]
        visited[0] = True
        stack.append(0)

        self.subtree_values[0].append((self.node_values[0], 0))

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

                for path_node in stack:
                    self.subtree_values[path_node].append((self.node_values[neighbor], neighbor))
            else:
                popped = stack.pop()

        # print(self.subtree_values)

        return self.subtree_values

    def get_xor_min(self, v, k):
        """
        Returns:
            tuple: max_value, max_vertex

        Comments:
            max_vertex: 0 indexed
        """

        # Get values of all nodes in the subtree rooted at v
        subtree_values_vertices = self.subtree_values[v]

        # Get Trie of binary of all these values
        if v not in self.subtree_tries:
            curr_trie = Trie()
            for value, vertex in subtree_values_vertices:
                bin_value = f'{value:020b}'  # exactly 20 length binary
                curr_trie.insert(bin_value, vertex)

            self.subtree_tries[v] = curr_trie
        else:
            curr_trie = self.subtree_tries[v]

        # Get max value by traversing the Trie and fetch largest vertex number
        binary_k = f'{k:020b}'
        root = curr_trie.root
        for bi in binary_k:
            int_bi = int(bi)
            not_int_bi = int(not int_bi)
            if not_int_bi in root.children:
                root = root.children[not_int_bi]
            else:
                root = root.children[int_bi]

        curr_values = root.vertices
        max_vertex = max(curr_values)
        max_value = k ^ self.node_values[max_vertex]

        return max_value, max_vertex


for _ in range(int(input())):
    N, Q = list(map(int, input().strip().split()))
    w = list(map(int, input().strip().split()))

    if N > 1:
        g = Graph(w)
        for _ in range(N - 1):
            ui, vi = list(map(int, input().strip().split()))
            g.add_edge(ui - 1, vi - 1)

        # pre-processing
        g.get_subtree_values()

        val_l = 0
        vert_l = -1
        for _ in range(Q):
            a, b = list(map(int, input().strip().split()))

            v = a ^ (vert_l + 1)
            k = b ^ val_l

            val_l, vert_l = g.get_xor_min(v - 1, k)  # 0-indexed

            print("{} {}".format(vert_l + 1, val_l))
    else:
        val_l = 0
        vert_l = 0
        for _ in range(Q):
            a, b = list(map(int, input().strip().split()))

            v = a ^ vert_l
            k = b ^ val_l

            print("{} {}".format(v, w[0] ^ k))


"""
1
10 5
9 17 93 16 3 61 23 11 2 1
1 2
2 5
5 8
1 3
1 4
3 6
3 7
6 9
6 10
4 14
7 123
5 103
9 32
5 118

"""