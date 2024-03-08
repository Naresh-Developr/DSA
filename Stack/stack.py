#implementing stack with List:

stack = [1,2,3,4,5,6]

print(stack[-1]) #acessing operation

stack.append(5) # Insertion operation

print(stack[-1])

stack.pop()   #deletion operation

print(stack)

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

#implementing Satck with dequeue:

from collections import deque  # to use dequeue.

#deque is a type of collection method

stack = deque([1,2,3,4,5])

print(stack[-1]) #accessing

stack.append(7) # insertion

stack.appendleft(0) # resversing of stack
