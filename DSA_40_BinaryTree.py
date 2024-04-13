
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None :
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def print_linked_list(self):
        if self.left:
            self.left.print_linked_list()
        print(self.data)
        if self.right :
            self.right.print_linked_list()



root = Node(10)
root.insert(20)
root.insert(10)
root.insert(7)
root.insert(9)
root.insert(8)
root.print_linked_list()

