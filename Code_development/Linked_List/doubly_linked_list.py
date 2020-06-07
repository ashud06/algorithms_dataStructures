class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
    def setData(self,data):
        self.data=data
    def getData(self):
        return self.data
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

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        length=0
    def insertAtBeginning(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=self.tail=newNode
        else:
            newNode.setPrev(None)
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head=newNode
    def insertAtEnd(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            self.tail=self.head
        else:
            current=self.head
            while current.hasNext():
                current=current.getNext()
            current.setNext(newNode)
            newNode.prev=current
            self.tail=current.getNext()
    def getNode(self,index):
        if self.head==None:
            return None
        current=self.head
        i=0
        while i<index:
            current=current.getNext()
            if current==None:
                break
            i+=1
        return current

    def insertAtGivenPosition(self,index,data):
        newNode=Node(data)
        if self.head==None or index==0:
            self.insertAtBeginning(data)
        elif index>0:
            temp=self.getNode(index)
            if temp==None or not temp.hasNext():
                self.insertAtEnd(data)
            else:
                newNode.setNext(temp.getNext())
                newNode.setPrev(temp)
                temp.getNext().setPrev(newNode)
                temp.setNext(newNode)
    def deleteAtGivenPosition(self,index):
        temp=self.getNode(index)
        if temp:
            temp.getPrev().setNext(temp.getNext())
            if temp.getNext():
                temp.getNext().setPrev(temp.getPrev())
            temp.setPrev(None)
            temp.setNext(None)
            temp.setData(None)
    def deleteGivenData(self,data):
        temp=self.head
        while temp is not None:
            if str(temp.getData())==str(data):
                if temp.hasPrev():
                    temp.getPrev().setNext(temp.getNext())
                    temp.getNext().setPrev(temp.getPrev())
                elif temp.hasNext():
                    self.head=temp.getNext()
                    temp.getNext().setPrev(None)
                else:
                    self.head=None
            temp=temp.getNext()
    def printList(self):
        current=self.head
        print("*********")
        while current is not None:
            print(current.getData())
            current=current.getNext()
        print("*********")

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
DL=DoubleLinkedList()
DL.insertAtBeginning(node1)
DL.printList()
#DL.insertAtEnd(node2)
#DL.insertAtEnd(node3)
#DL.insertAtEnd(node4)
#DL.printList()
#DL.deleteGivenData(1)
#DL.printList()
#DL.deleteAtGivenPosition(2)
#DL.insertAtEnd(5)
DL.deleteAtGivenPosition(2)
DL.printList()
DL.insertAtGivenPosition(2,4)
DL.printList()
