from singly_linked_list import Node, SinglyLinkedList

class AddRemoveProblems:
    def __init__(self):
        pass

    def add_node_at_nth_pos(self, data, pos):

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

    def remove_node_with_val(self, data):
        pass

    def remove_nth_node(self):
        pass