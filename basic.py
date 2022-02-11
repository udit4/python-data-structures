

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name


#               10
#       5               15
#   2       6       13      100
#
#

node = Node(10)
node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(100)


mytree = Tree(node, 'udit tree')

print(mytree.root.left.left.data)


#
