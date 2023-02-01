class LinkListNode:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode



node1=LinkListNode("3")
node2=LinkListNode("5")
node3=LinkListNode("7")
node1.nextNode=node2
node2.nextNode=node3



currentnode=node1
while True:
    print (currentnode.value,"->",end=" ")
    if currentnode.nextNode is None:
        print("None \n")
        break
    currentnode=currentnode.nextNode
    
