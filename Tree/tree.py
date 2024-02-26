#implementaion of Tree Data Structure: [[Add,and creation od node]].

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
    




tree = Tree()
tree.add(5)
tree.add(5,5)
tree.add(7,5)
tree.add(8,5)
tree.add(10,8)
