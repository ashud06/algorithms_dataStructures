#Node of a singly linked list
class Node:
    #constructor
    def __init__(self,data=None,next=None):
        self.data= data
        self.next= next
    #funx to set data in the node
    def setData(self,data):
        self.data= data
    #func to get data in the node
    def getData(self):
        return self.data
    #set next field of the node
    def setNext(self,next):
        self.next=next
    #get next field of the node
    def getNext(self):
        return self.next
    #returns true if node has a next
    def hasNext(self):
        return self.next!=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.length=0
    def getListLength(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count
    def insertAtBeginning(self,node):
        print('beg func. List length:{}'.format(self.length))
        if self.head:
            node.setNext(self.head)
            self.head=node
        else:
            self.head=node
        self.length+=1
    def insertAtEnd(self,node):
        print('end func. List length:{}'.format(self.length))
        current=self.head
        if current:
            while current.hasNext():
                current=current.getNext()
            current.setNext(node)
        else:
            self.head=node
        self.length += 1
    def printList(self):
        current=self.head
        while current:
            print current.data
            current=current.getNext()
    def insertAtPos(self,pos,node):
        print('length:{}'.format(self.length))
        if pos==0:
            self.insertAtBeginning(node)
        elif pos==self.length:
            self.insertAtEnd(node)
        else:
            current=self.head
            count=0
            while count<pos-1:
                current=current.getNext()
                count+=1
            node.setNext(current.getNext())
            current.setNext(node)
            self.length+=1
    def deleteAtBeginning(self):
        if self.head:
            self.head=self.head.getNext()
            self.length-=1
        else:
            print('This list is empty')
    def deleteAtEnd(self):
        if self.head:
            current=self.head
            while current.hasNext():
                prev=current
                current=current.getNext()
            prev.setNext(None)
            self.length -= 1
        else:
            print('List is empty')
    def deleteAtPos(self,pos):
        if pos> self.length or pos<0:
            print('Position doesnt exist. Enter a valid position')
        else:
            count=0
            prev=self.head
            current=self.head
            while count<pos or current.hasNext():
                count+=1
                if count==pos:
                    prev.setNext(current.getNext())
                    self.length-=1
                    return
                else:
                    prev=current
                    current=current.getNext()
    def deleteNode(self,node):
        if self.head:
            found= False
            current=self.head
            prev=None
            while not found:
                if current==node:
                    found= True
                elif current==None:
                    raise ValueError('Node not found in the linked list')
                    break
                else:
                    prev=current
                    current=current.getNext()
            if prev:
                prev.setNext(current.getNext())
                self.length -= 1
            else:
                self.head=current.getNext()
        elif self.length==0:
            raise ValueError('List is empty')
    def deleteList(self):
        self.head=None





LL=LinkedList()
myNode=Node(3)
LL.insertAtPos(0,myNode)
LL.printList()
print('------')
LL.insertAtBeginning(Node(5))
LL.printList()
print('------')
LL.insertAtEnd(Node(7))
LL.printList()
print('-------')
print(LL.length)
LL.insertAtPos(2,Node(16))
LL.printList()
print('--------')
LL.deleteAtBeginning()
LL.printList()
print('---------')
LL.deleteNode(myNode)
LL.printList()
print('----------')
LL.deleteAtPos(2)
LL.printList()