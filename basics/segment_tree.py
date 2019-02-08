class SegmentTree:
    def __init__(self, array):
        self.tree = [None] * 4 * len(array)
        self.array = array
        self.build(0, len(array) - 1, 0)

    def build(self, start, end, node):
        if end == start:
            self.tree[node] = self.array[start]
            return
        elif start > end:
            return

        mid = int( (start + end ) / 2 )

        self.build(start, mid, 2*node + 1)
        self.build(mid+1, end, 2*node + 2)

        self.tree[node] = self.tree[2*node + 1] + self.tree[2 * node + 2]

    def query(self, qlow, qhigh):
        # range sum
        return self. query_helper(qlow, qhigh, 0, len(self.array) - 1, 0)

    def query_helper(self, qlow, qhigh, low, high, pos):
        if qlow <= low and qhigh >= high:
            return self.tree[pos]

        if qlow > high or qhigh < low:
            return 0

        mid = int((low + high) / 2)

        return self.query_helper(qlow, qhigh, low, mid, 2*pos + 1) + self.query_helper(qlow, qhigh, mid+1, high, 2*pos + 2)

    def update(self, idx, value):
        diff = value - self.array[idx]
        self.array[idx] = value
        self.update_helper(idx, diff, 0, len(self.array) - 1, 0)

    def update_helper(self, idx, diff, start, end, pos):
        if idx < start or idx > end:
            return

        self.tree[pos] += diff
        if start != end:
            mid = int((start + end) / 2)
            self.update_helper(idx, diff, start, mid, 2*pos + 1)
            self.update_helper(idx, diff, mid+1, end, 2*pos + 2)


arr=[1,2,3,4,5,6]
st = SegmentTree(arr)
print(st.tree)

print(st.query(1,3))
st.update(0,4)
print(st.tree)