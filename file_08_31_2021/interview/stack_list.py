class Stack():
    def __init__(self):
        self.stack =list()
    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if(len(self.stack)>0):
            self.stack.pop()
        else:
            return None
    def peek(self):
        if(len(self.stack)>0):
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self): # print out the string representation of the list
        return str(self.stack)


my =Stack()
my.push(3)
my.push(8)
my.push(90)
print(my.__str__())
print(my.peek())
