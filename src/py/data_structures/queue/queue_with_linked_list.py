from data_structures.linked_list.doubly_linked_list.doubly_linked_list import Node, DoublyLinkedList

class Queue(DoublyLinkedList):
    def __init__(self, max_size=5):
        super(Queue, self).__init__()
        self.container_length = 0
        self.MAXSIZE = max_size

    def is_empty(self):
        return self.container_length == 0

    def is_full(self):
        return self.container_length == self.MAXSIZE

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full, nothing to enqueue")
            return
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.container_length += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, nothing to dequeue")
            return
        dequeued_element = self.head.data
        self.head = self.head.next
        self.head.prev = None

        self.container_length -= 1

        return dequeued_element

    def get_front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.head.data

    def get_rear(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.tail.data

    def size(self):
        return self.container_length

    def print_list(self):
        ptr = self.head
        res = "HEAD(front) <==> "
        while ptr:
            res += str(ptr.data) + " <==> "
            ptr = ptr.next
        res += "TAIL(rear)"
        print(res)

if __name__ == '__main__':
    print("Building Queue...")
    q = Queue(max_size=5)
    val_list = [2, 3, 4, 5, 6, 7]
    for val in val_list:
        q.enqueue(val)

    q.print_list()

    print("Front: ", q.get_front())
    print("Rear: ", q.get_rear())
    q.print_list()

    print("Dequeing...")
    print(q.dequeue())
    print(q.dequeue())
    q.print_list()
    print("Front: ", q.get_front())
    print("Rear: ", q.get_rear())

    q.enqueue(7)
    q.enqueue(8)
    q.print_list()

    print("Front: ", q.get_front())
    print("Rear: ", q.get_rear())

    print("Size: ", q.size())
    q.print_list()
