class Node :
    def __init__(self,data):
        self.left = None
        self.right = None
        self.value = data

class BinaryTree:
    def populate_rootnode(self):
        data = int(input("Enter the root Node \n"))
        root = Node(data)
        self.populate(root)
        self.print_binary_tree(root,"")

    def populate(self,node):
        left = input(f"Do you want to enter in the left of {node.value} \n")
        if left=="True":
            value = int(input(f"Enter the value you want to insert at left of {node.value} \n"))
            node.left = Node(value)
            self.populate(node.left)

        right = input(f"Do you want to enter in the right of {node.value} \n")
        if right=="True":
            value = int(input(f"Enter the value you want to insert at right of {node.value} \n"))
            node.right = Node(value)
            self.populate(node.right)

    def print_binary_tree(self,node,indent):
        if node == None :
            return 
        print(node.value)
        self.print_binary_tree(node.left,indent+"\t")
        self.print_binary_tree(node.right,indent+"\t")
        


tree = BinaryTree()
tree.populate_rootnode()







