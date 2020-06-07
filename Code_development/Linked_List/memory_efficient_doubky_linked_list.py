class Node:
    def __init__(self,data=None):
        self.data=data
        self.ptrdiff=None

    def setData(self,data):
        self.data=data
    def getData(self):
        return self.data
    def setPtrDiff(self,ptrDiff):
        self.ptrdiff=ptrDiff
    def getPtrDiff(self):
        return self.ptrdiff

class DoubleList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newNode=Node(data)
        global obj_id_dic
        obj_id_dic[id(newNode)]=newNode
        if self.head==None:
            self.head=newNode
            self.head.setPtrDiff(0)
        else:
            newNode.setPtrDiff(id(self.head))
            self.head.setPtrDiff(XOR(id(newNode),XOR(None,self.head.getPtrDiff())))
            self.head=newNode
            obj = obj_id_dic[self.head.getPtrDiff()]



    def printList(self):
        global obj_id_dic
        if self.head==None:
            print "lsit is empty"
            return
        current=self.head
        prev=None
        next=None
        while current!=None:
            print obj_id_dic[id(current)].getData()
            next=XOR(current.getPtrDiff(),prev)
            prev=current
            for key,val in obj_id_dic.items():
                if val==prev:
                    prev=key
            try:
                current=obj_id_dic[next]
            except:
                current=None

def XOR(val1,val2):
    if val1==None:
        val1=0
    if val2==None:
        val2=0
    return val1 ^ val2



count=0
obj_id_dic={}

List=DoubleList()
List.insert(1)
List.insert(2)
List.insert(3)
List.insert(8)
List.insert(9)
List.insert(9)
List.printList()


