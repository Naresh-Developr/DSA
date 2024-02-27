#imbalanced Tree implementation 
# implement of Add and dispaly.

class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self,data):
        if not self.root:
            self.root = Node(data)
            return
        self.recursive(data,self.root) 
        # if self.root:
        #     if data > self.root:
        #         node.left = data
        #     else:
        #         node.right = data
    
    def recursive(self,data,node):
        if node.left is  None:
            node.left = Node(data)
        elif node.right is  None:
            node.right = Node(data)
        else:
            self.recursive(data,node.left)     #recursive alert

    def display(self,depth=0,node=None):
        if node is  None:
            node = self.root

        print(" " * depth, node.data)

        if node.left is not None:
            self.display(depth+1,node.left)
        if node.right is not None:
            self.display(depth+1,node.right)

    def delete(self,data):
        if not self.root:
            print("Binary tree was empty")
            return
        if self.root.data == data:
            self.root = None
            return
        self.recursiveRemove(data,self.root)
        
    def recursiveRemove(self,data,node):

        if node.left and node.left.data == data:  # checks for not None
            node.left = None
            return
        if node.right and node.right.data == data:
            node.right = None
            return
        if node.left:
            self.recursiveRemove(data,node.left)
        if node.right:
            self.recursiveRemove(data,node.right)

    def search(self,data):
        nodeFound = self.recursiveSearch(data,self.root)

        if nodeFound:
            print("True")
        else:
            print("False")

    def recursiveSearch(self,data,node):
        if not node or node.data == data:
            return node
        return self.recursiveSearch(data,node.left) or self.recursiveSearch(data,node.right)
    

    




t = BinaryTree()
t.add(1)
t.add(2)
t.add(3)
t.add(4)
t.add(6)
t.add(7)
t.display()
t.search(2)

#debug it to understand and use paper/pen method.


