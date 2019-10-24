import copy

class queue:
    def __init__(self):
        self.storage = []
        self.size = 0

    def push(self, x):
        self.storage.append(x)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.storage.pop(0)

    def front(self):
        if self.empty():
            return None
        else:
            return self.storage[0]

    def back(self):
        if self.empty():
            return None
        else:
            return self.storage[self.size - 1]

    def empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def trav(self):
        for i in self.storage:
            print(i, end=' ')
        print('')

    def __getitem__(self, i):
        return self.storage[i]



if __name__ == '__main__':
    q = queue()

    for i in range(1,16,2):
        q.push(i)
        # print(q.back(), q.size)

    # q.trav()

    q2 = copy.deepcopy(q)

    while not q.empty():
        print(q.pop(), end=' ')

    print("\nq2:")

    for i in range(q2.size):
        print(q2[i], end=' ')

    print('')

class deque(queue):
    def push_back(self, x):
        self.push(x)

    def pop_front(self):
        return self.pop()

    def push_front(self, x):
        self.size += 1
        self.storage.insert(0, x)
    
    def pop_back(self):
        self.size -= 1
        return self.storage.pop()


if __name__ == '__main__':
    dq = deque()

    for i in range(10):
        dq.push_back(i)

    dq.trav()

    for i in range(10):
        dq.push_front(i)

    dq.trav()

    for i in range(10):
        dq.pop_back()

    dq.trav()

    for i in range(10):
        dq.pop_front()

    dq.trav()