class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    def Print_LL(self):
        if self.head is None:
            print("The link list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref
            print("\n")
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node


    def add_end(self,data):
        new_node=Node(data)
        n=self.head
        while n.ref !=None:
            n=n.ref
        n.ref=new_node


    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref
        if n is None:
            print("Item is Not Present in the linked list")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not found !")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node


    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("\n")
            print("Linked list is not empty ")


    def delete_begin(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            self.head=self.head.ref
    
    def delete_end(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    def delete_by_value(self,x):
        if self.head==None:
            print("Linked List is Empty")
            return 
        if self.head==x:
            self.head=self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data ==x:
                break
            n=n.ref
        if n.ref ==None:
            print("No node is found")
        else:
            n.ref=n.ref.ref

    def Print_reverse_link_list(self):
        cur=self.head
        prev=None
        while cur!=None:
            temp=cur.ref
            cur.ref=prev
            prev=cur
            cur=temp
        # return prev
        while prev.ref!=None:
            print(prev.data,"---->",end=" ")
            prev=prev.ref


    def reverse_link_list(self,mid):
        cur=mid
        prev=None
        while cur!=None:
            temp=cur.ref
            cur.ref=prev
            prev=cur
            cur=temp
        return prev

    def getIndex(self, index):
        val=1
        n=self.head
        while n!=None:
            if val==index:
                break
            val+=1
            n=n.ref
        if val==index:
            return n.data


    def FindMid(self):
        f=self.head
        s=self.head
        while f!=None and f.ref!=None:
            s=s.ref
            f=f.ref.ref
        return s
        

        
    def PalindromeCheck(self):
        if self.head ==None:
            return True
        Mid=self.FindMid()
        last=self.reverse_link_list(Mid)
        cur=self.head
        while last!=None:
            if last.data !=cur.data:
                return False
            last=last.ref
            cur=cur.ref
        return True


    def getMid(self):
        s=self.head
        f=self.head
        while f!=None and f.ref!=None :
            s=s.ref
            f=f.ref.ref
        return s
        

    def get_index_of_num(self,num):
        if self.head==None:
            return
        if self.head.data==num:
            return 0
        count=0
        n=self.head
        while n!=None:
            if n.data==num:
                return count
            count+=1
            n=n.ref
        return -1




    def Count__LL(self):
        count=0
        n=self.head
        while n!=None:
            count+=1
            n=n.ref
        return count


    def Delete_LL_From_last(self,num):
        count=self.Count__LL()
        index=(count-num)+1
        print(index)
        if self.head==None:
            return None
        if self.head.ref==None and index==1:
            return None
        if index==1:
            self.head=self.head.ref 
            return   
        count=1
        n=self.head
        while count+1!=index:
            count+=1
            n=n.ref
        n.ref=n.ref.ref
            
            
    def getsum_of_linklist(self):
        if self.head==None:
            return None
        Sum=0
        node=self.head
        while node!= None:
            # Sum+= node.data
            Sum=Sum*10+node.data
            node=node.ref  
        print(Sum)
            
        
        











LL1=LinkedList()
LL1.add_begin(1)
LL1.add_end(2)
LL1.add_end(3)
LL1.add_end(4)
LL1.add_end(5)
LL1.getsum_of_linklist()
# LL1.Print_LL()
# LL1.deleteindex(2)
# LL1.Delete_LL_From_last(2)

# LL1.add_end(4)
# LL1.add_end(7)
# LL1.add_end(1)
# LL1.add_end(2)
# LL1.add_end(6)
LL1.Print_LL()



