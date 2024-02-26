#method 1

queue = []

#enqueue operation:
queue.append(5)
queue.append("value")
queue.append(3)

#deque operation
a = queue.pop(0)
b = queue.pop(1)

print(a,b)

#Front

print(queue[0])

#isempty

print(len(queue)==0)
