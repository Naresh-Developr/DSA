#method 2

from queue import Queue

q = Queue() #q = Queue(maxsize=3)  --> syntax to declare size in queue


q.put(2)
q.put("name")
q.put(3)

a = q.get()
print(a)

#Front

print(q.queue[0])  #syntax to access first element in queue

#isempty

print(q.empty()) # --> return True if values present