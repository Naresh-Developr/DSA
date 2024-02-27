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
           




t = BinaryTree()
t.add(1)
t.add(2)
t.add(3)
t.add(4)
t.add(6)
t.add(7)
t.display()

