from data_structures.linked_list.doubly_linked_list.doubly_linked_list import Node, DoublyLinkedList


class Stack(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.container_length = 0

    def is_empty(self):
        return self.head is None and self.tail is None

    def push(self, data):
        node = Node(data)
        if self.container_length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.container_length += 1

    def pop(self):
        if self.container_length == 0:
            print("Stack is empty, nothing to pop")
            return

        popped_element = self.tail.data
        self.container_length -= 1
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return popped_element

    def size(self):
        return self.container_length

    def top(self):
        if self.container_length == 0:
            print("Stack is empty, Nothing present")
            return
        return self.tail.data

    def empty(self):
        self.head = None
        self.tail = None

    def print_stack_elements(self):
        res = ""
        for idx in reversed(range(self.container_length)):
            res += str(self.container[idx]) + " "

        print(res)



if __name__ == '__main__':
    stack = Stack()

    val_list = [2, 4, 3, 5, 7, 9]
    for val in val_list:
        stack.push(val)

    stack.print_list()
    print("Top: ", stack.top())
    print("Pop: ", stack.pop())
    print("Top: ", stack.top())
    print("Size: ", stack.size())
    stack.print_list()

    stack.push(9)
    stack.print_list()

    for i in range(2):
        print(stack.pop())

    print("Top: ", stack.top())
    print("Size: ", stack.size())
    stack.print_list()
    stack.empty()
    stack.print_list()

