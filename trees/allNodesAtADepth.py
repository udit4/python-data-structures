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

    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        return

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()
        return

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)
        return

    def height(self, h=0):
        if self.left:
            leftHeight = self.left.height(h+1)
        else:
            leftHeight = h

        if self.right:
            rightHeight = self.right.height(h+1)
        else:
            rightHeight = h

        return max(leftHeight, rightHeight)

    def allNodesAtDepth(self, depth, nodes = []):
        if depth==0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.allNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))

        if self.right:
            self.right.allNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        return nodes

class Tree:
    def __init__(self, node, name=''):
        self.root = node
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def preorder(self):
        return self.root.preorder()

    def inorder(self):
        return self.root.inorder()

    def postorder(self):
        return self.root.postorder()

    def height(self):
        return self.root.height()

    def allNodesAtDepth(self, depth):
        return self.root.allNodesAtDepth(depth)

#                   10
#           5               15
#       2       6       13      100
#   1
#

node = Node(10)
node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(100)
node.left.left.left = Node(1)

mytree = Tree(node, 'udit tree')
print(mytree.allNodesAtDepth(3))
