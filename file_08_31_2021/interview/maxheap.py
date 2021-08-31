'''
Max Heap is completelt a binary tree
every node is lessthen or equl to parent node
everytime we pop a item from a heap it will be the highest number in the max heap

A maxheap alwys bubbles or floats the higest value to the top
so it can be removed instantly.
Public function push,peek,pop
private funtions: swap, __floatUp, __bubbleDown, __str
'''
class Maxheap():
    def __init__(self,items=[]):
        self.heap=[0] # we dont use this as we start from 1
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap)-1)
    def push(self,data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return None
    def pop(self):
        if(len(self.heap)>2):
            self.__swap(1,len(self.heap)-1)
            max =self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) ==2:
            max =self.heap.pop()
        else:
            max = False
        return max
    def __swap(self,i,j):
        self.heap[i],self.heap[j] =self.heap[j],self.heap[i]
    def __floatUp(self,index):
        parent =index//2
        if index <=1:
            return
        elif self.heap[index] >self.heap[parent]:
            self.__swap(index,parent)
            self.__floatUp(parent)
    def __bubbleDown(self,index):
        left =index*2
        right = index*2 +1
        largest =index
        if len(self.heap)> left and self.heap[largest] <self.heap[left]:
            largest =left
        if len(self.heap)> right and self.heap[largest] <self.heap[right]:
            largest=right
        if largest != index:
            self.__swap(index,largest)
            self.__bubbleDown(largest)
    def __str__(self):
        return str(self.heap)

m_heap =Maxheap()
m_heap.push(25)
m_heap.push(11)
m_heap.push(16)
m_heap.push(24)
m_heap.push(5)
print(m_heap.__str__())