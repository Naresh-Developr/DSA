class Node:
    def __init__(self,data):
        self.data = data
        self.pointer = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,data):
        newNode = Node(data)
        if self.head is  None:
            self.head = newNode
        else: 
            cur = self.head
            while(cur.pointer is not None):
                cur = cur.pointer
            cur.pointer = newNode

    def print(self):
        cur = self.head
        while(cur is not None):
            print(f"-->{cur.data}",end="")
            cur = cur.pointer
        print()
    
    def remove(self,data):
        if(self.head is not None):
            if(self.head.data==data):
                self.head = self.head.pointer
            else:
                cur = self.head

                while(cur.pointer is not None and cur.pointer.data != data):
                    cur = cur.pointer
                
                cur.pointer = cur.pointer.pointer
        else:
            print("The Linked list is empty.")





linkedList = LinkedList()
linkedList.add(10)
linkedList.add(11)
linkedList.add(12)
linkedList.add(13)
linkedList.add(14)
linkedList.print()
linkedList.remove(12)
linkedList.print()