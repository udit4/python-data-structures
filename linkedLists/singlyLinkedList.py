

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

    def size(self):
        size, tempNode = 0, self
        while tempNode is not None:
            size+=1
            tempNode = tempNode.next
        return size

    def addNode(self, node):
        tempNode = self
        while tempNode.next is not None:
            tempNode = tempNode.next
        tempNode.setNextNode(node)
        return



class LinkedList:
    def __init__(self, node=None, name=''):
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

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def addFront(self, node):
        newHeadNode = node
        newHeadNode.next = self.head
        self.head = newHeadNode
        return

    def size(self):
        return self.head.size()

    def addNode(self):
        return self.head.addNode()


head = Node(10)
head.addNode(Node(20))
head.addNode(Node(30))
head.addNode(Node(40))


list = LinkedList(head)

list.addFront(Node(0))
list.traverse()
