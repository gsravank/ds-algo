class Queue:

    def __init__(self):
        self.push_stack = list()
        self.get_stack = list()
        return

    def push(self, elem):
        self.push_stack.append(elem)
        return

    def get(self):
        if len(self.get_stack) == 0:
            while len(self.push_stack) != 0:
                self.get_stack.append(self.push_stack.pop())

        if len(self.get_stack) != 0:
            return self.get_stack.pop()

        return


q = Queue()

q.push(1)
q.push(2)
q.push(3)
print(q.get())
print(q.get())
q.push(4)
q.push(5)
print(q.get())
print(q.get())
print(q.get())
print(q.get())