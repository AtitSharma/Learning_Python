class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    

    def MergeLL(self,node1,node2):
        if node1==None  and node2==None:
            return None
        if node1==None:
            return node2
        if node2==None:
            return node1
        if node1.data < node2.data:
            temp=node1
            temp.next=self.MergeLL(node1.next,node2)
        else:
            temp=node2
            temp.next=self.MergeLL(node1,node2.next)
        return temp

    def getMid(self,head):
        s=head
        f=head
        while f!=None and f.next!=None :
            s=s.next
            f=f.next.next
        return s
    def add_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node


    def Print_Link(self):
        if self.head==None:
            print("Empty")
        else:
            n=self.head
            while n!=None:
                print(n.data,"-->",end=" ")
                n=n.next


LL1=LinkedList()
LL1.add_begin(9)
LL1.add_begin(8)
LL1.add_begin(7)
LL1.add_begin(6)
LL1.add_begin(5)
LL1.Print_Link()
