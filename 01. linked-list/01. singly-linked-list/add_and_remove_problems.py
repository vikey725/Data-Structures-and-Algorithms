from singly_linked_list import Node, SinglyLinkedList

class AddRemoveProblems(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def validator(self, pos):
        if pos < 0:
            print(f"Pos cant be less than 0, but {pos} given")
            return False
        if pos > self.get_length():
            print(f"Pos cant be greater than the list length: {self.get_length()}, "
                             f"but {pos} given")
            return False
        return True

    def add_node_at_nth_pos(self, data, pos):
        if not self.validator(pos):
            return
        # create a node
        node = Node(data)

        # We don't want to change head, so we take a ptr
        # variable to point to same location as head, and
        # modify it
        ptr = self.head
        if pos == 0:

            # to insert at 0th position, we can assign the ptr
            # to the next of node, and change the head to point to
            # the node
            node.next = ptr
            self.head = node
        else:
            cnt = 1
            while ptr:

                # Reach to the position where cnt == pos and make node's next
                # point to ptr's next and make ptr's next point to node
                if cnt == pos:
                    node.next = ptr.next
                    ptr.next = node
                    break
                ptr = ptr.next
                cnt += 1

    def delete_node_with_val(self, data):
        ptr = self.head
        flag = False
        if ptr.data == data:
            flag = True
            self.head = self.head.next
        else:
            while ptr.next:
                if ptr.next.data == data:
                    flag = True
                    ptr.next = ptr.next.next
                    break
                ptr = ptr.next

        if not flag:
            print(f"{data} not present in the linked list")

    def delete_nth_node(self, pos):
        if not self.validator(pos):
            return

        ptr = self.head
        if pos == 0:
            self.head = self.head.next
        else:
            cnt = 1
            while ptr.next:
                if cnt == pos:
                    ptr.next = ptr.next.next
                    break
                ptr = ptr.next
                cnt += 1

    def add_node_at_nth_pos_from_last_v1(self, data, pos):
        if not self.validator(pos):
            return
        # The easiest way is to find the position from the start and
        # convert the problem to nth node from the start
        length = self.get_length()
        pos = length - pos
        self.add_node_at_nth_pos(data, pos)

    def add_node_at_nth_pos_from_last_v2(self, data, pos):
        if not self.validator(pos):
            return
        node = Node(data)
        ptr1 = self.head
        ptr2 = None
        cnt = 0
        while ptr1:
            if cnt >= pos:
                if ptr2 is None:
                    ptr2 = self.head
                else:
                    ptr2 = ptr2.next
            ptr1 = ptr1.next
            cnt += 1

        if ptr2 is None:
            node.next = self.head
            self.head = node
        else:
            node.next = ptr2.next
            ptr2.next = node

    def delete_node_at_nth_pos_from_last_v1(self, pos):
        if not self.validator(pos):
            return
        # The easiest way is to find the position from the start and
        # convert the problem to nth node from the start
        length = self.get_length()
        pos = length - pos - 1
        self.delete_nth_node(pos)

    def delete_node_at_nth_pos_from_last_v2(self, pos):
        if not self.validator(pos+1):
            return
        ptr1 = self.head
        ptr2 = None
        cnt = 0
        while ptr1.next:
            if cnt >= pos:
                if ptr2 is None:
                    ptr2 = self.head
                else:
                    ptr2 = ptr2.next
            ptr1 = ptr1.next
            cnt += 1

        if ptr2 is None:
            self.head = self.head.next
        else:
            ptr2.next = ptr2.next.next

if __name__ == '__main__':

    # Creating linked list
    val_list = [2, 3, 5, 7, 10]
    add_remove_obj = AddRemoveProblems()
    for val in val_list:
        add_remove_obj.add_node(val)
    print("Created a Linked List:")
    add_remove_obj.print_list()

    # Add node at nth pos
    print("*" * 20)
    val_and_pos_list = [(1, 0), (6, 4), (11, 7)]
    for val, pos in val_and_pos_list:
        print(f"Adding node with value {val} at {pos}th pos...")
        add_remove_obj.add_node_at_nth_pos(val, pos)
        add_remove_obj.print_list()

    # delete nodes with val
    print("*" * 20)
    val_list = [1, 6, 11, 25]
    for val in val_list:
        print(f"Deleting node with val {val}...")
        add_remove_obj.delete_node_with_val(val)
        add_remove_obj.print_list()

    # delete nodes at with val
    print("*" * 20)
    pos_list = [0, 1, 2, 14]
    for pos in pos_list:
        print(f"Deleting node at {pos}th pos...")
        add_remove_obj.delete_nth_node(pos)
        add_remove_obj.print_list()

    # Add node at nth pos from the last V1
    print("*" * 20)
    val_and_pos_list = [(1, 0), (6, 1), (11, 4), (15, 10)]
    for val, pos in val_and_pos_list:
        print(f"Adding node with value {val} at {pos}th pos from last...")
        add_remove_obj.add_node_at_nth_pos_from_last_v1(val, pos)
        add_remove_obj.print_list()

    # Add node at nth pos from the last V2
    print("*" * 20)
    val_and_pos_list = [(10, 0), (5, 1), (17, 7)]
    for val, pos in val_and_pos_list:
        print(f"Adding node with value {val} at {pos}th pos from last...")
        add_remove_obj.add_node_at_nth_pos_from_last_v2(val, pos)
        add_remove_obj.print_list()

    # Delete node at nth pos from the last V1
    print("*" * 20)
    pos_list = [0, 3, 5]
    for pos in pos_list:
        print(f"Removing node at {pos}th pos from last...")
        add_remove_obj.delete_node_at_nth_pos_from_last_v1(pos)
        add_remove_obj.print_list()

    # Delete node at nth pos from the last V1
    print("*" * 20)
    pos_list = [0, 3, 1]
    for pos in pos_list:
        print(f"Removing node at {pos}th pos from last...")
        add_remove_obj.delete_node_at_nth_pos_from_last_v2(pos)
        add_remove_obj.print_list()




