


#CREATING A NODE
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
#TRAVARSING A LINK BETWEEN A NODE 
class LinkedList:
    def __init__(self):
        self.head=None
    def Print_LL(self):
        if self.head is None:
            print("The LL is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.ref
n1=Node(7)
S1=LinkedList()
S1.head=n1
n2=Node(10)
n1.ref=n2
n3=Node(14)
n2.ref=n3
n4=Node(17)
n3.ref=n4
S1.Print_LL()
