

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            return True

        if self.data > target and self.left != None:
            return self.left.search(target)

        if self.data < target and self.right != None:
            return self.right.search(target)

        return False


class Tree:
    def __init__(self, node, name=''):
        self.root = node
        self.name = name

    def search(self, target):
        return self.root.search(target)

#               10
#       5               15
#   2       6       13      100
#


node = Node(10)
node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(100)

mytree = Tree(node, 'udit tree')

print(mytree.search(2))
