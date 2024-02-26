#implementaion of Tree Data Structure: [[print and remove of element]].

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

    def add(self,data,parentData=None):
        node = TreeNode(data)

        if not self.root:  #to check root is empty or not
            self.root = node
            return
        parentNode = self.findNode(parentData,self.root)

        if not parentNode:
            print("parentNode was not Found")
            return

        parentNode.children.append(node)

    def findNode(self,data,node): #node specifies the root node here
        if node.data == data:
            return node
        
        for i in node.children:  # recursive alert!!! recursive checks for each elment and pass to findNode function.
            nodeFound = self.findNode(data,i) # i specifiess the child in the children list.
            if nodeFound:
                return nodeFound
        
        return None 
    def display(self,depth=0,node=None):
        if not node:
            node = self.root
        if not node:
            return

        print(" " * depth,node.data)
        for i in node.children:
            self.display(depth+1,i)  #recusive alert!!!

    def remove(self,data):
        if not self.root:
            print("There is no root element ")
            return
        if self.root.data == data:
            self.root = None
            return
        
        parentNode = self.findParentNode(data,self.root)
        
        if parentNode:
            #print(parentNode.children)
            for child in parentNode.children:
                if child.data == data:
                    parentNode.children.remove(child)
                    return
        print("Node not found")




    def findParentNode(self,data,node):
        for child in node.children:
            if child.data == data:
                return node  
            nodeFound = self.findParentNode(data,child) 
            if nodeFound:
                return nodeFound
        return None

        

    
tree = Tree()
tree.add(1)
tree.add(2,1)
tree.add(3,1)
tree.add('a',1)
tree.add(4,2)
tree.add(5,2)
tree.add(6,3)
tree.add(7,3)
tree.display()
tree.remove('a')
print("\n")
print("\n")
tree.display()