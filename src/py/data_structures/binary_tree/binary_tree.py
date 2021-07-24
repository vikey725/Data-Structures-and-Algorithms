from data_structures.stack.stack_with_array import Stack

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, node_ptr: Node, data: object, direction: str=None):
        node = Node(data)
        if node_ptr == None:
            self.root = node
        else:
            if direction == "L":
                node_ptr.left = node
            elif direction == "R":
                node_ptr.right = node
            else:
                print(f"Direction should be between L and R but {direction} given")
                raise ValueError(f"Direction should be between L and R but {direction} given")

    def get_target_node_ptr(self, target_node_direction):
        print(target_node_direction)
        target_node_ptr = self.root
        for direction in target_node_direction:
            if direction == "L":
                target_node_ptr = target_node_ptr.left
            elif direction == "R":
                target_node_ptr = target_node_ptr.right
            else:
                raise ValueError(f"Target node direction should have onlu L and R but {direction} given")

        return target_node_ptr

    def make_tree(self, tree_structure):
        # target_node_direction, data, direction
        for data, target_node_direction, direction in tree_structure:
            target_node_ptr = self.get_target_node_ptr(target_node_direction)
            self.add_node(target_node_ptr, data, direction=direction)

    def inorder(self, ptr, res):
        if ptr is not None:
            self.inorder(ptr.left, res)
            res.append(ptr.data)
            self.inorder(ptr.right, res)

    def preorder(self, ptr, res):
        if ptr is not None:
            res.append(ptr.data)
            self.preorder(ptr.left, res)
            self.preorder(ptr.right, res)

    def postorder(self, ptr, res):
        if ptr is not None:
            self.postorder(ptr.left, res)
            self.postorder(ptr.right, res)
            res.append(ptr.data)

    def inorder_without_recursion(self, ptr, res):
        stack = Stack()
        while True:
            if ptr is not None:
                stack.push(ptr)
                ptr = ptr.left
            elif not stack.is_empty():
                ptr = stack.pop()
                res.append(ptr.data)
                ptr = ptr.right
            else:
                break

    def preorder_without_recursion(self, ptr, res):
        stack = Stack()
        while True:
            if ptr is not None:
                res.append(ptr.data)
                stack.push(ptr)
                ptr = ptr.left
            elif not stack.is_empty():
                ptr = stack.pop()
                ptr = ptr.right
            else:
                break

    def postorder_without_recursion(self, ptr, res):
        stack = Stack()
        while True:
            while(ptr):
                stack.push(ptr)
                stack.push(ptr)
                ptr = ptr.left

            if stack.is_empty():
                return
            ptr = stack.pop()
            if stack.size() > 0 and stack.top() == ptr:
                ptr = ptr.right
            else:
                res.append(ptr.data)
                ptr = None

    def postorder_without_recursion_v2(self, ptr, res):
        stack = Stack()
        while True:
            while(ptr):
                if ptr.right:
                    stack.push(ptr.right)
                stack.push(ptr)
                ptr = ptr.left

            if stack.is_empty():
                return
            ptr = stack.pop()

            if not stack.is_empty() and stack.top() == ptr.right:
                stack.pop()
                stack.push(ptr)
                ptr = ptr.right
            else:
                res.append(ptr.data)
                ptr = None





if __name__ == '__main__':

    bt = BinaryTree()
    tree_structure = [(1, "", ""), (2, "", "L"), (3, "", "R"), (4, "L", "L"),
                      (5, "L", "R"), (6, "R", "L"), (7, "R", "R"), (9, "LL", "R"),
                      (10, "LR", "L"), (14, "RR", "L")]
    bt.make_tree(tree_structure)

    print("Inorder: ")
    inorder_list = []
    bt.inorder(bt.root, inorder_list)
    print(inorder_list)

    print("Inorder without recursion: ")
    inorder_list = []
    bt.inorder_without_recursion(bt.root, inorder_list)
    print(inorder_list)

    print("Preorder: ")
    preorder_list = []
    bt.preorder(bt.root, preorder_list)
    print(preorder_list)

    print("Preorder without recursion: ")
    preorder_list = []
    bt.preorder_without_recursion(bt.root, preorder_list)
    print(preorder_list)

    print("Postorder: ")
    postorder_list = []
    bt.postorder(bt.root, postorder_list)
    print(postorder_list)

    print("Postorder without recursion: ")
    postorder_list = []
    bt.postorder_without_recursion(bt.root, postorder_list)
    print(postorder_list)

    print("Postorder without recursion V2: ")
    postorder_list = []
    bt.postorder_without_recursion_v2(bt.root, postorder_list)
    print(postorder_list)