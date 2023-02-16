class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


my_tree = BinarySearchTree()
my_tree.insert(25)
my_tree.insert(15)
my_tree.insert(10)
my_tree.insert(4)
my_tree.insert(12)
my_tree.insert(22)
my_tree.insert(18)
my_tree.insert(24)
my_tree.insert(50)
my_tree.insert(35)
my_tree.insert(31)
my_tree.insert(44)
my_tree.insert(70)
my_tree.insert(66)
my_tree.insert(90)
my_tree.insert(60)


"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""

print('Root:', my_tree.root.value)
print('Root->Left:', my_tree.root.left.value)
print('Root->Right:', my_tree.root.right.value)
print(my_tree.root.right.right.value)
