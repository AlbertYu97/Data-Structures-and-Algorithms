class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root == None:
            self.root = new_node
            return
        temp = self.root
        while True:
            if new_node.val < temp.val:
                if temp.left == None:
                    temp.left = new_node
                    break
                else:
                    temp = temp.left
            elif new_node.val > temp.val:
                if temp.right == None:
                    temp.right = new_node
                    break
                else:
                    temp = temp.right

    def lookup(self, val):
        temp = self.root
        while True:
            if temp.val == val:
                return True
            elif temp == None:
                return False
            elif val < temp.val:
                temp = temp.left
            elif val > temp.val:
                temp = temp.right

    def breadth_first_search(self):
        current_node = self.root
        list = []
        # queue can get large, memory consumption is a problem
        queue = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.val)
            list.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return list

    def breath_first_search_recursive(self, queue, list):
        if not len(queue):
            return list
        current_node = queue.pop(0)
        print(current_node.val)
        list.append(current_node.val)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        return self.breath_first_search_recursive(queue, list)


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

x = tree.lookup(170)
print(x)
# print(tree.breadth_first_search())
print(tree.breath_first_search_recursive([tree.root], []))
