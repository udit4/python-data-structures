

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

    def search(self, value):
        tempNode = self
        while tempNode is not None:
            if tempNode.data == value:
                return True
            else:
                tempNode = tempNode.next
        return False

    def removeNode(self, value):
        tempNode = self
        # case 1 :: when the node does not exist in the list or list is empty
        exists = self.search(value)
        if not exists:
            print("node with value does not exist in the list")
            return
        else:
            tempNode = self
            # case 2 :: when the node is the head node
            if tempNode.data == value:
                nextNode = self.getNextNode()
                self.data, self.next = nextNode.data, nextNode.next
                return
            # case 3 :: when the node is somwhere else in the list
            prevNode = None
            while tempNode.data != value:
                prevNode = tempNode
                tempNode = tempNode.next
            prevNode.next = tempNode.next
            return
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

    def removeNode(self, value):
        return self.head.removeNode(value)


head = Node(10)
head.addNode(Node(20))
head.addNode(Node(30))
head.addNode(Node(40))


list = LinkedList(head)

list.addFront(Node(0))
list.traverse()

list.removeNode(0)
list.traverse()

list.removeNode(40)
list.removeNode(100)
list.traverse()
