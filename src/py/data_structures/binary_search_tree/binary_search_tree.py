class Node:
    def __init__(self, key, data=""):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data=""):
        node = Node(key, data)

        if not self.root:
            self.root = node
        else:
            ptr = self.root
            while True:
                if key <= ptr.key:
                    if ptr.left:
                        ptr = ptr.left
                    else:
                        ptr.left = node
                        break
                else:
                    if ptr.right:
                        ptr = ptr.right
                    else:
                        ptr.right = node
                        break

    def get_no_of_child(self, ptr):
        if ptr.left and ptr.right:
            return 2
        elif not ptr.left and not ptr.right:
            return 0
        else:
            return 1

    def get_inorder_predecessor(self, prev, ptr):
        while ptr.right:
            prev = ptr
            ptr = ptr.right
        return prev, ptr


    def remove(self, ptr, key):
        if not ptr:
            print(f"{key} not present in the tree")
            return ptr

        if key < ptr.key:
            ptr.left = self.remove(ptr.left, key)
            return ptr
        if key > ptr.key:
            ptr.right = self.remove(ptr.right, key)
            return ptr

        if not ptr.left and not ptr.right:
            if ptr == self.root:
                self.root = None
            return None

        if not ptr.left:
            if ptr == self.root:
                self.root = ptr.right
            tmp = ptr.right
            return tmp

        if not ptr.right:
            if ptr == self.root:
                self.root = ptr.left
            tmp = ptr.left
            return tmp

        in_pred_parent, in_pred = self.get_inorder_predecessor(ptr, ptr.left)
        print(ptr.key, in_pred_parent.key, in_pred.key)

        if in_pred_parent != ptr:
            in_pred_parent.right = in_pred.left
        else:
            in_pred_parent.left = in_pred.left

        ptr.key = in_pred.key

        return ptr

    def find(self):
        pass

    def inorder(self, ptr, res):
        if ptr:
            self.inorder(ptr.left, res)
            res.append((ptr.key, ptr.data))
            self.inorder(ptr.right, res)


if __name__ == '__main__':
    bst = BinarySearchTree()
    key_and_name_list = [(5, "Vikash"), (3, "Vishal"), (7, "Adarsh"), (2, "Aniruddha"),
                         (4, "Pratyush"), (6, "Sarvesh"), (8, "Bhai"), (9, "Altaaf")]
    for key, name in key_and_name_list:
        bst.insert(key, data=name)

    res = []
    bst.inorder(bst.root, res)
    print(res)

    bst.remove(bst.root, 9)
    res = []
    bst.inorder(bst.root, res)
    print(res)





