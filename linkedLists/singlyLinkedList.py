

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, value):
        self.data = value
        return

    def getNextNode(self):
        return self.next

    def setNextNode(self, node):
        self.next = node
        return

    def traverse(self):
        tempNode = self
        while tempNode is not None:
            print(tempNode.data)
            tempNode = tempNode.next
        return


class LinkedList:
    def __init__(self, node, name=''):
        self.head = node
        self.name = name

    def getData(self):
        return self.head.getData()

    def setData(self, value):
        return self.head.setData()

    def getNextNode(self):
        return self.head.getNextNode()

    def setNextNode(self, node):
        return self.head.setNext(node)

    def traverse(self):
        return self.head.traverse()




head = Node(10)
head.setNextNode(Node(20))
head.getNextNode().setNextNode(Node(30))
head.getNextNode().getNextNode().setNextNode(Node(40))

list = LinkedList(head)
list.traverse()
