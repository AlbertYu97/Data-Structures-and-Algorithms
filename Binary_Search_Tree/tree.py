class BinaryTreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None

class BinarySearchTree:
    def __init__(self, li=None):
        self.root = None
        if li:
            for var in li:
                self.insert_no_rec(var)

    # Recursion
    # def insert(self, node, value):
    #     if not node:
    #         node = BinaryTreeNode(value)
    #     elif value < node.value:
    #         node.left = self.insert(node.left, value)
    #         node.left.parent = node
    #     elif value > node.value:
    #         node.right = self.insert(node.right, value)
    #         node.right.parent = node
    #     return node

    def insert_no_rec(self, value):
        p = self.root
        if not p: # Empty tree
            self.root = BinaryTreeNode(value)
            return
        while True:
            if value < p.value:
                if p.left: # If left child exists, move to left child
                    p = p.left
                else: # If left child DNE, then insert
                    p.left = BinaryTreeNode(value)
                    p.left.parent = p
            elif value > p.value:
                if p.right:
                    p = p.right
                else:
                    p.right = BinaryTreeNode(value)
                    p.right.parent = p
            else:
                return


    def search(self, value):
        p = self.root
        while p:
            if value < p.value:
                p = p.left
            elif value > p.value:
                p = p.right
            else:
                return p
        return None

    def remove_node_1(self, node):
        # node has no child
        if not node.parent: # root
            self.root = None
        if node == node.parent.left:
            node.parent.left = None
        else: # right child
            node.parent.right = None

    def remove_node_21(self, node):
        # node has only 1 left child
        if not node.parent: #root
            self.root = node.left
            node.lchild.parent = None
        elif node == node.parent.left:
            node.parent.left = node.left
            node.left.parent = node.parent
        else:
            node.parent.right = node.left
            node.left.parent = node.parent

    def remove_node_22(self, node):
        # node has only 1 right child
        if not node.parent:
            self.root = node.right
        elif node == node.parent.left:
            node.parent.left = node.right
            node.right.parent = node.parent
        else:
            node.parent.right = node.right
            node.right.parent = node.parent

    def delete(self, value):
        if self.root: # Non-empty tree
            node = self.search(value)
            if not node: # DNE
                return False
            if not node.left and not node.right:
                # no child
                self.remove_node_1(node)
            elif not node.right:
                # only left child
                self.remove_node_21(node)
            elif not node.left:
                # only right child
                self.remove_node_22(node)
            else:
                # has both left and right child, find min node in right child
                min_node = node.right
                while min_node.left:
                    min_node = min_node.left
                node.value = min_node.value # sub min value
                # del min node based on if the right child exist
                if min_node.right:
                    self.remove_node_22(node)
                else:
                    self.right


    def pre_order(self, root):
        if root:
            print(root.value, end=',)
            self.pre_order(root.left)
            self.pre_order(root.right)

                tree = BinarySearchTree([4,6,7,9,2,1,3,5,8])
tree.pre_order(tree.root)
print(tree.search(8))

