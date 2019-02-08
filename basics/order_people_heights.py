class SegmentTree:
    def __init__(self, array):
        self.tree = [0] * 4 * len(array)
        self.array = array
        self.build(0, len(array) - 1, 0)

    def build(self, start, end, node):
        if end == start:
            # keep count of number of empty slots in the array
            # empty slot means that value in array is -1 at that position
            if self.array[start] == -1:
                self.tree[node] = 1
            else:
                self.tree[node] = 0
            return
        elif start > end:
            return

        mid = int((start + end) / 2)

        self.build(start, mid, 2*node + 1)
        self.build(mid+1, end, 2*node + 2)

        self.tree[node] = self.tree[2*node + 1] + self.tree[2 * node + 2]

    def update(self, idx, value):
        if value != -1:
            if self.array[idx] == -1:
                diff = -1
            else:
                diff = 0
        else:
            if self.array[idx] == -1:
                diff = 0
            else:
                diff = 1

        self.array[idx] = value

        if diff != 0:
            self.update_helper(idx, diff, 0, len(self.array) - 1, 0)

    def update_helper(self, idx, diff, start, end, pos):
        if idx < start or idx > end:
            return

        self.tree[pos] += diff
        if start != end:
            mid = int((start + end) / 2)
            self.update_helper(idx, diff, start, mid, 2*pos + 1)
            self.update_helper(idx, diff, mid+1, end, 2*pos + 2)

    def get_position(self, count):
        if count <= 0 or count > self.tree[0]:
            return None

        return self.get_position_helper(0, len(self.array) - 1, 0, count)

    def get_position_helper(self, start, end, pos, count):
        if start == end:
            return start

        mid = int((start + end) / 2)

        if count <= self.tree[2 * pos + 1]:
            return self.get_position_helper(start, mid, 2*pos + 1, count)
        else:
            return self.get_position_helper(mid+1, end, 2*pos + 2, count - self.tree[2 * pos + 1])


arr = [-1, -1, -1, -1, -1]
st = SegmentTree(arr)
print(st.tree)

# print(st.query(1,3))
# st.update(0,4)
# print(st.tree)
# st.update(0, -1)
# print(st.tree)

print(st.get_position(1))