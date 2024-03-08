#Test implementaion of Linked List:

class Node:

    def __init__(self,data):
        self.data = data
        self.pointer = None

node1 = Node(None)
node2 = Node(20)
node1.pointer = node2
# node3 = Node(30)
# node1.pointer = node2
# node2.pointer = node3

print(node1.data)
print(node1.pointer)
print(node2.data)
# cur = node1

# while(cur is not None):
#     print(cur.data)
#     cur = cur.pointer

         