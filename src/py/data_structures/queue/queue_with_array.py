class Queue:
    def __init__(self, max_size=5):
        self.MAXSIZE = max_size
        self.container = []
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        return (self.rear+1) % self.MAXSIZE == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full, nothing to enqueue")
            return
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.MAXSIZE

        if len(self.container) < self.MAXSIZE:
            self.container.append(data)
        else:
            self.container[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, nothing to dequeue")
            return
        elif self.front == self.rear:
            dequeued_element = self.container[self.front]
            self.front = self.rear = -1
        else:
            dequeued_element = self.container[self.front]
            self.front = (self.front + 1) % 5

        return dequeued_element

    def get_front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.container[self.front]

    def get_rear(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.container[self.rear]

    def size(self):
        return (self.MAXSIZE + self.rear - self.front) % self.MAXSIZE + 1

    def print_queue(self):
        res = ""
        for idx in range(self.size()):
            idx = (idx + self.front) % self.MAXSIZE
            res += str(self.container[idx]) + " "

        print(res)


if __name__ == '__main__':
    q = Queue(max_size=5)
    val_list = [2, 3, 4, 5, 6, 7]
    for val in val_list:
        q.enqueue(val)

    print("Front: ", q.get_front())
    print("Rear: ", q.get_rear())
    q.print_queue()

    print(q.dequeue())
    print(q.dequeue())
    print("Front: ", q.get_front())
    print("Rear: ", q.get_rear())

    q.enqueue(7)
    q.enqueue(8)

    print("Front: ", q.get_front())
    print("Rear: ", q.get_rear())

    print("Size: ", q.size())


