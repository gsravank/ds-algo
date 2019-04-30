from collections import defaultdict


class Graph:
    def __init__(self, node_values):
        self.graph = defaultdict(lambda: list())
        self.node_values = node_values
        self.subtree_sums = list()
        self.neg_set = dict()
        self.subtree_mins = list()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def get_subtree_sums(self):
        m = len(self.graph)
        self.subtree_sums = self.node_values[:]

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
            else:
                popped = stack.pop()

                if len(stack):
                    self.subtree_sums[stack[-1]] += self.subtree_sums[popped]

        # print("Subtree sums: {}".format(self.subtree_sums))
        return self.subtree_sums

    def get_answer(self, k):
        m = len(self.graph)

        neg_sums = [0 for _ in range(m)]
        neg_counts = [0 for _ in range(m)]

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
            else:
                popped = stack.pop()

                subtree_neg_sum = neg_sums[popped]
                subtree_neg_count = neg_counts[popped]
                popped_node_subtree_sum = self.subtree_sums[popped]

                if popped_node_subtree_sum < subtree_neg_sum + ((subtree_neg_count - 1) * k):
                    neg_sums[popped] = popped_node_subtree_sum
                    neg_counts[popped] = 1
                else:
                    pass

                if len(stack):
                    top = stack[-1]

                    neg_sums[top] += neg_sums[popped]
                    neg_counts[top] += neg_counts[popped]

        # print("Neg sums: {}".format(neg_sums))
        # print("Neg counts: {}".format(neg_counts))

        return self.subtree_sums[0] - ( neg_sums[0] + (k*neg_counts[0]) )


for _ in range(int(input())):
    N, X = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))

    if N > 1:
        g = Graph(A)
        for _ in range(N - 1):
            ui, vi = list(map(int, input().strip().split()))
            g.add_edge(ui - 1, vi - 1)

        g.get_subtree_sums()
        max_profit = g.get_answer(X)

        print(max_profit, flush=True)
    else:
        if A[0] < (-1 * X):
            print(-1 * X)
        else:
            print(A[0])


"""
1
3 5
1 -5 -10
1 2
2 3

"""

"""
1
6 0
24 13 -3 -20 -7 3
1 2
1 5
2 3
2 4
5 6

"""

"""
2
6 15
24 13 -3 -20 -7 3
1 2
1 5
2 3
2 4
5 6
6 0
24 13 -3 -20 -7 3
1 2
1 5
2 3
2 4
5 6

"""


"""
1
11 0
27 0 5 -15 -30 11 -9 5 20 -6 2
1 2
1 3
2 4
2 5
3 6
3 7
4 8
5 9
6 10
7 11

"""