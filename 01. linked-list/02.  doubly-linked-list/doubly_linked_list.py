class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_length(self):
        ptr = self.head
        length = 0
        while ptr:
            length += 1
            ptr = ptr.next
        return length

    def add_node(self, data):
        node = Node(data)

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next

            node.prev = ptr
            ptr.next = node
            self.tail = node

    def delete_node_with_val(self, data):
        if self.head is None and self.tail is None:
            print("The list is empty")
            return
        ptr = self.head
        flag = False
        if ptr.data == data:
            self.head = self.head.next
            self.head.prev = None
            flag = True
        else:
            while ptr:
                if ptr.next is None:
                    break
                if ptr.next.data == data:
                    ptr.next = ptr.next.next
                    if ptr.next is not None:
                        ptr.next.prev = ptr
                    flag = True
                ptr = ptr.next

        if not flag:
            print(f"{data} not present in the list")

    def add_node_at_nth_pos(self, data, pos):
        node = Node(data)
        ptr = self.head
        if pos == 0:
            if self.head is None and self.tail is None:
                self.head = node
                self.tail = node
            else:
                node.next = self.head
                self.head.prev = node
                self.head = node
        else:
            cnt = 1
            while ptr:
                if cnt == pos:
                    node.next = ptr.next
                    if ptr.next is not None:
                        ptr.next.prev = node
                    else:
                        self.tail = node
                    ptr.next = node
                    node.prev = ptr
                cnt += 1
                ptr = ptr.next

    def add_node_at_nth_pos_from_last(self, data, pos):
        node = Node(data)
        ptr = self.tail
        if pos == 0:
            if self.head is None and self.tail is None:
                self.head = node
                self.tail = node
            else:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
        else:
            cnt = 1
            while ptr:
                if cnt == pos:
                    node.prev = ptr.prev
                    if ptr.prev is not None:
                        ptr.prev.next = node
                    else:
                        self.head = node
                    ptr.prev = node
                    node.next = ptr
                cnt += 1
                ptr = ptr.prev

    def delete_node_at_nth_pos(self, pos):

        if self.head is None and self.tail is None:
            print("List is empty, nothing to delete")
            return

        cnt = 0
        ptr = self.head
        while ptr:
            if cnt == pos:
                if ptr.next is not None:
                    ptr.next.prev = ptr.prev
                else:
                    self.tail = ptr.prev

                if ptr.prev is not None:
                    ptr.prev.next = ptr.next
                else:
                    self.head = ptr.next
            ptr = ptr.next
            cnt += 1

    def delete_node_at_nth_pos_from_last(self, pos):
        if self.head is None and self.tail is None:
            print("List is empty, nothing to delete")
            return

        cnt = 0
        ptr = self.tail
        while ptr:
            if cnt == pos:
                if ptr.prev is not None:
                    ptr.prev.next = ptr.next
                else:
                    self.head = ptr.next

                if ptr.next is not None:
                    ptr.next.prev = ptr.prev
                else:
                    self.tail = ptr.prev
            ptr = ptr.prev
            cnt += 1


    def print_list(self):
        ptr = self.head
        res = "None <==> "
        while ptr:
            res += str(ptr.data) + " <==> "
            ptr = ptr.next
        res += "None"
        print(res)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    val_list = [2, 3, 4, 5, 7]
    print("Creating doubly linked list...")
    for val in val_list:
        ll.add_node(val)
    ll.print_list()

    # Delete node
    val_list = [2, 4, 7, 10]
    for val in val_list:
        print(f"deleting {val} from the list...")
        ll.delete_node_with_val(val)
        ll.print_list()

    # Add node at nth pos
    val_and_pos_list = [(1, 0), (2, 1), (7, 4)]
    for val, pos in val_and_pos_list:
        print(f"Adding {val} at pos {pos}...")
        ll.add_node_at_nth_pos(val, pos)
        ll.print_list()

    # Add node at nth pos
    val_and_pos_list = [(8, 0), (9, 1), (10, 7)]
    for val, pos in val_and_pos_list:
        print(f"Adding {val} at pos {pos} from the last...")
        ll.add_node_at_nth_pos_from_last(val, pos)
        ll.print_list()

    pos_list = [0, 2, 5]
    for pos in pos_list:
        print(f"Deleeting node at pos {pos}...")
        ll.delete_node_at_nth_pos(pos)
        ll.print_list()

    pos_list = [0, 2, 2]
    for pos in pos_list:
        print(f"Deleeting node at pos {pos} from last...")
        ll.delete_node_at_nth_pos_from_last(pos)
        ll.print_list()










