class BSTNode:

    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def add(self,data):
        if not self.root:
            self.root = BSTNode(data)
            return
        self.recursiveAdd(data,self.root)


    def recursiveAdd(self,data,node):
        if data < node.data:
            if not node.left:
                node.left = BSTNode(data)
            else:
                self.recursiveAdd(data,node.left)
        
        elif data > node.data:
            if not node.right:
                node.right = BSTNode(data)
            else:
                self.recursiveAdd(data,node.right)
    def display(self):
        result = []
        self.inorderTraversal(self.root,result)
        print(result)

    def inorderTraversal(self,node,result):
        if not node:
            return None
        else:
            self.inorderTraversal(node.left,result)
            result.append(node.data)
            self.inorderTraversal(node.right,result)
    
    def preOrderTraversal(self,node,result):
        if not node:
            return None
        else:
            result.append(node.data)  #current
            self.inorderTraversal(node.left,result) #left
            self.inorderTraversal(node.right,result) #right

    def postOrderTraversal(self,node,result):
        if not node:
            return None
        else:
            self.inorderTraversal(node.left,result) #left
            self.inorderTraversal(node.right,result) #right
            result.append(node.data)  #current

    def remove(self,data):
        if not self.root:
            print("No Elements")
            return
        
        if self.root.data == data:
            self.root = None
            return
        self.recursiveRemove(data,self.root)
        
    def recursiveRemove(self,data,node):
        if node.left and node.left.data == data:
            node.left = None
            return
        elif node.right and node.right.data == data:
            node.right = None
            return
        elif data < node.data:
            self.recursiveRemove(data,node.left)
        elif data > node.data:
            self.recursiveRemove(data,node.right)

    def search(self,data):
        node  =  self.recursiveSearch(data,self.root)
        if node:
            print("true")
        else:
            print("false")

    def recursiveSearch(self,data,node):
        if not node:
            return node
        if node and node.data == data:
            return node
        elif data > node.data:
            return self.recursiveSearch(data,node.right)
        elif data < node.data:
            return self.recursiveSearch(data,node.left)

        
        


        



b =  BinarySearchTree()
b.add(10)
b.add(18)
b.add(17)
b.add(12)
b.add(13)
b.add(11)
b.display()
b.remove(12)
b.display()
b.search(17)

        
        
