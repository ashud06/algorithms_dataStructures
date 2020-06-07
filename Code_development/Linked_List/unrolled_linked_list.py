class Node:
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next

class LinkedBlock:
    def __init__(self):
        self.head=None
        self.next=None
        self.nodeCount=0

blockSize=4
blockHead=None

def newLinkedBlock():
    block=LinkedBlock()
    block.head=None
    block.next=None
    block.nodeCount=0
    return block

def newNode(val):
    temp=Node()
    temp.next=None
    temp.value=val
    return temp

def searchElements(blockHead,k):
    global blockSize
    #kth element is in jth block
    j=(k+blockSize-1)//blockSize
    p=blockHead
    j-=1
    while(j):
        p=p.next
        j-=1
    fLinkedBlock=p
    #find the node
    q=p.head
    k=k%blockSize
    if k==0:
        k=blockSize
    #k=p.nodeCount-1+k
    k-=1
    while(k):
        q=q.next
        k-=1
    fNode=q
    return fLinkedBlock,fNode

def shift(A):
    B=A
    global blockHead
    global blockSize
    while(A.nodeCount>blockSize):
        if A.next==None:
            A.next=newLinkedBlock()
            B=A.next
            temp=A.head.next
            A.head.next=A.head.next.next
            B.head = temp
            temp.next=B.head.next
            B.head.next=temp
            B.head=temp
            A.nodeCount-=1
            B.nodeCount+=1

        else:
            B=A.next
            temp=A.head.next
            A.head.next=A.head.next.next
            temp.next=B.head.next
            B.head.next=temp
            B.head=temp
            A.nodeCount-=1
            B.nodeCount+=1
        A=B
def insertElement(k,x):
    global blockHead
    if blockHead==None:
        blockHead=newLinkedBlock()
        blockHead.head=newNode(x)
        blockHead.head.next=blockHead.head
        blockHead.nodeCount+=1
    else:
        #special case where k=0
        if k==0:
            p=blockHead.head
            q=p.next
            p.next=newNode(x)
            p.next.next=q
            blockHead.head=p.next
            blockHead.nodeCount+=1
            shift(blockHead)
        else:
            r,p=searchElements(blockHead,k)
            print 'return val: {}'.format(p.value)
            q=p
            while q.next!=p:
                q=q.next
            q.next=newNode(x)
            q.next.next=p
            r.nodeCount+=1
            shift(r)
    return blockHead

def searchElement(blockHead,k):
    q,p=searchElements(blockHead,k)
    return p.value

def printUnrolledList(blockHead):
    p=blockHead
    while p!=None:
        count=p.nodeCount
        q=p.head
        print '--------'
        while count:
            print q.value
            q=q.next
            count-=1
        print '---------'
        p=p.next

blockHead=insertElement(0,1)
blockHead=insertElement(0,2)
blockHead=insertElement(0,3)
printUnrolledList(blockHead)
blockHead=insertElement(1,4)
#blockHead=insertElement(1,5)

printUnrolledList(blockHead)
print searchElement(blockHead,0)
