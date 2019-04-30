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

    # def get_subtree_sums_aux(self, v, visited):
    #     visited[v] = True
    #     # print(visited)
    #
    #     # Get sum of all values in sub-tree rooted at v
    #     curr_sum = self.node_values[v]
    #     for i in self.graph[v]:
    #         if not visited[i]:
    #             curr_sum += self.get_subtree_sums_aux(i, visited)
    #
    #     self.subtree_sums[v] = curr_sum
    #     # print(self.subtree_sums)
    #     return curr_sum

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

        print("Subtree sums: {}".format(self.subtree_sums))
        return self.subtree_sums

    # def get_negative_set_aux(self, v, visited, k):
    #     visited[v] = True
    #
    #     # Get minimum value in the sub-tree rooted at v
    #     curr_min = self.subtree_sums[v]
    #     for i in self.graph[v]:
    #         if not visited[i]:
    #             curr_min = min(curr_min, self.get_negative_set_aux(i, visited, k))
    #
    #     if self.subtree_sums[v] == curr_min < (-1*k):
    #         self.neg_set[v] = curr_min
    #
    #     return curr_min

    def get_negative_set(self, k):
        m = len(self.graph)
        stack = list()
        visited = [False for _ in range(m)]
        visited[0] = True
        stack.append(0)

        self.subtree_mins = self.subtree_sums[:]
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
                    self.subtree_mins[stack[-1]] = min(self.subtree_mins[stack[-1]], self.subtree_mins[popped])

        for v in range(m):
            if self.subtree_sums[v] == self.subtree_mins[v] < (-1 * k):
                self.neg_set[v] = self.subtree_mins[v]

        print("Subtree Mins: {}".format(self.subtree_mins))
        print("Neg-set: {}".format(self.neg_set))
        return self.neg_set

    # def get_negative_trim_set_aux(self, v, visited, parent):
    #     visited[v] = True
    #
    #     # Remove a value from neg_set if there is an ancestor which is also in neg_set
    #     # Subtree sum of ancestor in neg_set will always be less than current subtree sum
    #     # This is because neg_set is formed based on minimum of the subtree
    #     if parent is not None:
    #         if v in self.neg_set:
    #             self.neg_set[v] = 0
    #     else:
    #         if v in self.neg_set:
    #             parent = v
    #
    #     for i in self.graph[v]:
    #         if not visited[i]:
    #             self.get_negative_trim_set_aux(i, visited, parent)

    def get_negative_trim_set(self):
        m = len(self.graph)
        stack = list()
        visited = [False for _ in range(m)]
        visited[0] = True
        stack.append(0)

        if 0 in self.neg_set:
            parent = 0
        else:
            parent = None

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

                if parent is None:
                    if neighbor in self.neg_set:
                        parent = neighbor
                    else:
                        parent = None
                else:
                    pass
            else:
                popped = stack.pop()

                if popped == parent:
                    parent = None

                if popped in self.neg_set and parent is not None:
                    self.neg_set[popped] = 0

        print("Neg-set after trimming: {}".format(self.neg_set))
        return self.neg_set

    def get_max_profit(self, k):
        profit = self.subtree_sums[0]

        count = 0
        for key in self.neg_set:
            if self.neg_set[key] != 0:
                profit -= self.neg_set[key]
                count += 1

        profit -= (count * k)
        return profit


for _ in range(int(input())):
    N, X = list(map(int, input().strip().split()))
    A = list(map(int, input().strip().split()))

    if N > 1:
        g = Graph(A)
        for _ in range(N - 1):
            ui, vi = list(map(int, input().strip().split()))
            g.add_edge(ui - 1, vi - 1)

        g.get_subtree_sums()
        g.get_negative_set(X)
        g.get_negative_trim_set()
        max_profit = g.get_max_profit(X)

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