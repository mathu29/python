class Node:
    def __init__(self,d):
        self.data=d
        self.nxt=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insatbeg(self,data):
        newnode=Node(data)
        newnode.nxt=self.head
        self.head=newnode
    def delatbeg(self):
        newnode=self.head
        self.head=self.head.nxt
        newnode=None
    def printlist(self):
        newnode=self.head
        while newnode!=None:
            print(newnode.data,"==>",end='')
            newnode=newnode.nxt
llod=Linkedlist()        
ch=0
while ch!=4:
    print("enter the choice:1.Insertion 2.Deletion 3.Printlist 4.exit")
    ch=int(input())
    if ch==1:
        data=input()
        print("enter the node")
        llod.insatbeg(data)
        llod.printlist()
    elif ch==2:
        llod.delatbeg()
        llod.printlist()
    elif ch==3:
        llod.printlist()
