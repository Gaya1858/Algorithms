from collections import deque

my_queue = deque()

my_queue.append(3) # appends at the end of the queue--- acts as enqueue
my_queue.append(10)
my_queue.append(12)

print(my_queue)
print(my_queue.popleft()) # returns first item that has been added to the queue--- acts as dequeue
