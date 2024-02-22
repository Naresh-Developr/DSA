#Test implementaion of Linked List:

class Node:

    def __init__(self,data):
        self.data = data
        self.pointer = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.pointer = node2
node2.pointer = node3

cur = node1

while(cur is not None):
    print(cur.data)
    cur = cur.pointer

         