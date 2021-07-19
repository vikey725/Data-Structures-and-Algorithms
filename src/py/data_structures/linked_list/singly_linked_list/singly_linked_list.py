class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        length = 0

        # We don't want to change head, so we take a ptr
        # variable to point to same location as head, and
        # modify it
        ptr = self.head
        while ptr:
            length += 1
            ptr = ptr.next
        return length

    def add_node(self, data):
        node = Node(data)
        if self.head is None:

            # if list is empty, make node as head
            self.head = node
        else:

            # We don't want to change head, so we take a ptr
            # variable to point to same location as head, and
            # modify it
            ptr = self.head

            # move the ptr till we reach the last node
            while ptr.next:
                ptr = ptr.next

            # assign node to the next of last node
            ptr.next = node

    def print_list(self):
        res = ""
        ptr = self.head
        while ptr:
            res += str(ptr.data) + " ==> "
            ptr = ptr.next

        res += "None"
        print(res)

if __name__ == '__main__':
    ll = SinglyLinkedList()
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(4)
    ll.add_node(7)
    ll.add_node(10)
    ll.print_list()




