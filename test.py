# #a = int(input())
# n=5
# def r():
#     for i in range(1,n):
#         for j in range(1,0,-1):
#             print(i)
#             print(j)

# r()
# a = hash("Naresh");
# b = hash("suresh")
# print(a)
# print(b)

# l1 = [None,None,[["naresh",5]]]

# for count, ele in enumerate(l1):
#     print(count)
#     print(ele)

# def secondRun():
#     num = []

#     for i in range(5):
#         a = int(input())
#         num.append(a)
#     print(num)
#     num.sort()
#     print(max(num))
#     print(len(num)-2)


# secondRun()

# l = [1,1,2]
# l = list(set(l))
# print(l)
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

# Creating an empty linked list
my_list = LinkedList()

# Checking if the linked list is empty
if my_list.is_empty():
    print("The linked list is empty")
else:
    print("The linked list is not empty")