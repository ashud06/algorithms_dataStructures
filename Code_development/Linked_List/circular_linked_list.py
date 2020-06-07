class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
    def setData(self,data):
        self.data=data
    def getData(self):
        return self.datas
    def setNext(self,next):
        self.next=next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next!=None
    def setPrev(self,prev):
        self.prev=prev
    def getPrev(self):
        return self.prev
    def hasPrev(self):
        return self.prev!=None
    def __str__(self):
        return "%s"%(self.data)

class Circular_Linked_List:
    def __init__(self):
        self.head=None

    def getCircularLinkedListLength(self):
        currentNode=self.head
        if currentNode==None:
            return 0
        count=1
        currentNode=currentNode.getNext()
        while currentNode!=self.head:
            currentNode=currentNode.getNext()
            count+=1
        return count
    def printCircularLinkedList(self):
        current=self.head
        if current==None:
            print "list is empty"
            return
        print "########"
        print current.getData()
        current=current.getNext()
        while current!=self.head:
            if current:
                print current.getData()
                current=current.getNext()
            else:
                break
        print "########"
    def insertNodeAtEnd(self,data):
        current=self.head
        newNode=Node(data)
        newNode.setNext(newNode)
        if current==None:
            self.head=newNode
        else:
            while current.getNext()!=self.head:
                current=current.getNext()
                if current==None:
                    break
            current.setNext(newNode)
            newNode.setNext(self.head)
    def insertNodeAtFront(self,data):
        current=self.head
        newNode=Node(data)
        newNode.setNext(newNode)
        if self.head==None:
            self.head=newNode
        else:
            while current.getNext()!=self.head:
                current=current.getNext()
            newNode.setNext(newNode)
            newNode.setNext(self.head)
            current.setNext(newNode)
            self.head=newNode
    def deleteLastNode(self):
        current = self.head
        prev=self.head
        if current==None:
            print "List is empty"
            return
        else:
            while current.getNext()!=self.head:
                prev=current
                current=current.getNext()
            if current.getNext()!=current:
                prev.setNext(current.getNext())
            else:
                self.head=None
            return
    def deleteFirstNode(self):
        current=self.head
        if current==None:
            print "List is empty"
        else:
            while current.getNext()!=self.head:
                current=current.getNext()
            if current.getNext()!=current:
                current.setNext(self.head.getNext())
                self.head=self.head.getNext()
            else:
                self.head=None
            return

CLL=Circular_Linked_List()
#CLL.insertNodeAtEnd(1)
#CLL.insertNodeAtEnd(2)
CLL.insertNodeAtFront(1)
CLL.insertNodeAtEnd(3)
CLL.printCircularLinkedList()
CLL.deleteFirstNode()
CLL.printCircularLinkedList()
CLL.deleteLastNode()
CLL.printCircularLinkedList()
