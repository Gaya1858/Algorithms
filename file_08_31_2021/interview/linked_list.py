'''

this class will be wrapper class for singly linked list, doubly linked lisna dn circular linked lisk

'''

class Node:
    def __init__(self, data,next=None,pre=None):
        self.data=data
        self.next_node =next
        self.pre_node =pre
    def __str__(self):
        return ('('+str(self.data) +')')

class LinkedList:
    def __init__(self, root=None):
        self.root =root
        self.size =0
    def add(self,data):
        new_node =Node(data,self.root)
        self.root =new_node
        self.size+=1
    def find(self,d):
        this_node = self.root
        while this_node is not None:
            if this_node.data ==d:
                return d
            else:
                this_node =this_node.next_node
        return None
    def remove(self,d):
        this_node =self.root
        pre_node =None
        while this_node is not None:
            if this_node.data ==d:
                if(pre_node is not None):
                    pre_node.next_node =this_node.next_node
                else:
                    self.root =this_node.next_node
                self.size -=1
                return True
            else:
                pre_node =this_node
                this_node =this_node.next_node
            return False
    def print_list(self):
        this_node =self.root
        while this_node is not None:
            print(this_node,end='->')
            this_node=this_node.next_node
        print('None')


my_ll =LinkedList()
my_ll.add(5)
my_ll.add(10)
my_ll.add(19)
my_ll.print_list()
my_ll.remove(10)
my_ll.print_list()
