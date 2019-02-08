class MaxHeap:
    def __init__(self, heap=list()):
        self.heap = heap
        self.size = len(heap)
        self.build_max_heap()

    @staticmethod
    def left(i):
        return 2*i + 1

    @staticmethod
    def right(i):
        return 2*i + 2

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        max_idx = i
        if l <= self.size - 1:
            if self.heap[l] > self.heap[max_idx]:
                max_idx = l

        if r <= self.size - 1:
            if self.heap[r] > self.heap[max_idx]:
                max_idx = r

        if max_idx != i:
            self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
            self.heapify(max_idx)

    def build_max_heap(self):
        self.size = len(self.heap)
        for i in range(int(self.size / 2 ), -1, -1):
            self.heapify(i)

    def heap_sort(self):
        for _ in range(self.size - 1):
            self.heap[self.size - 1], self.heap[0] = self.heap[0], self.heap[self.size - 1]
            self.size -= 1
            self.heapify(0)

        return self.heap


class MinHeap:
    def __init__(self, heap=list()):
        self.heap = heap
        self.size = len(heap)
        self.build_min_heap()

    @staticmethod
    def left(i):
        return 2*i + 1

    @staticmethod
    def right(i):
        return 2*i + 2

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        max_idx = i
        if l <= self.size - 1:
            if self.heap[l] < self.heap[max_idx]:
                max_idx = l

        if r <= self.size - 1:
            if self.heap[r] < self.heap[max_idx]:
                max_idx = r

        if max_idx != i:
            self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
            self.heapify(max_idx)

    def build_min_heap(self):
        self.size = len(self.heap)
        for i in range(int(self.size / 2 ), -1, -1):
            self.heapify(i)

    def heap_sort(self):
        for _ in range(self.size - 1):
            self.heap[self.size - 1], self.heap[0] = self.heap[0], self.heap[self.size - 1]
            self.size -= 1
            self.heapify(0)

        return self.heap


import numpy as np

l = [10,9,8,7,6,5,4,3,2,1]
mh = MinHeap(heap=list(l))
print(mh.heap)