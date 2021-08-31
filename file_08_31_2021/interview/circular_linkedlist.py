
class Node:
    def __init__(self, data,next=None,pre=None):
        self.data=data
        self.next_node =next
        self.pre_node =pre
    def __str__(self):
        return ('('+str(self.data) +')')

class CircularLinkedList:
    def __init__(self, root=None):
        self.root =root
        self.size =0
    def add(self,data):
        if(self.size ==0):
            self.root =Node(data)
            self.root.next_node =self.root
        else:
            new_node =Node(data,self.root.next_node)
            self.root.next_node =new_node
        self.size+=1
    def find(self,d):
        this_node = self.root
        while True:
            if this_node.data ==d:
                return d
            elif this_node.next_node ==self.root:
                return False
            this_node =this_node.next_node

    def remove(self,d):
        this_node =self.root
        pre_node =None
        while True:
            if this_node.data ==d:
                if(pre_node is not None):
                    pre_node.next_node =this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node =this_node.next_node
                    this_node.next_node =self.root.next_node
                    self.root =self.root.next_node
                self.size -=1
                return True
            elif this_node.next_node ==self.root:
                return False

            pre_node =this_node
            this_node =this_node.next_node

    def print_list(self):
        if self.root is None:
            return
        this_node =self.root
        print(this_node,end='->')
        while this_node.next_node != self.root:
            this_node =this_node.next_node
            print(this_node,end='->')
        print()


my_ll =CircularLinkedList()
for i in [5,7,3,8,9]:
    my_ll.add(i)
print("size= "+ str(my_ll.size))
print(my_ll.print_list())
print(my_ll.find(8))
print(my_ll.find(12))
# looping continusly to see the circular list

my_node =my_ll.root
print(my_node,end='->')
for i in range(8):
    my_node=my_node.next_node
    print(my_node,end='->')
print()