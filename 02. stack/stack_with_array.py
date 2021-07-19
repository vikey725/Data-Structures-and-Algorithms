class Stack:
    def __init__(self):
        self.container = []
        self.container_length = 0

    def is_empty(self):
        return self.size() == 0

    def push(self, data):
        if self.container_length < len(self.container):
            self.container[self.container_length] = data
        else:
            self.container.append(data)
        self.container_length += 1

    def pop(self):
        if self.container_length == 0:
            print("Stack is empty, nothing to pop")
            return
        self.container_length -= 1
        return self.container[self.container_length]

    def size(self):
        return self.container_length

    def top(self):
        if self.container_length == 0:
            print("Stack is empty, nothing to pop")
            return
        return self.container[self.container_length-1]

    def empty(self):
        self.container = []
        self.container_length = 0

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

    stack.print_stack_elements()
    print("Top: ", stack.top())
    print("Pop: ", stack.pop())
    print("Top: ", stack.top())
    print("Size: ", stack.size())
    stack.print_stack_elements()

    stack.push(9)
    stack.print_stack_elements()

    for i in range(7):
        print(stack.pop())

    print("Top: ", stack.top())
    print("Size: ", stack.size())

