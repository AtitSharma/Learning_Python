class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None


class LinkedList:
    def __init__(self):
        self.head=None


    def Print_Linked_List (self):
        if self.head==None:
            print("Linked list is empty")
        n=self.head
        while n is not None:
            print(n.data,"---->",end=" ")
            n=n.ref

    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    
    def add_end(self,data):

        new_node=Node(data)
        n=self.head
        if n is None:
            print("Linked list is Empty")
            return
        while n.ref is not None:
            n=n.ref
        n.ref=new_node




    def Remove_duplicates(self):
        node=self.head
        while node.ref != None:
            if node.data==node.ref.data:
                node.ref=node.ref.ref
            else:
                node=node.ref




LL1=LinkedList()
LL1.add_begin(20)
LL1.add_begin(20)
LL1.add_begin(20)
LL1.add_end(30)
LL1.Remove_duplicates()
LL1.Print_Linked_List()


