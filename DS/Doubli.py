#Doubli Linked List Start ->

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None #Beginning of LL
        # self.prev = None #Ending of LL
        
    def Traverse_Forward(self):
        current = self.head
        while current:
            print(current.data, end='<-->')
            current = current.next
        print(None)

    def Traverse_Backward(self):
        current = self.head
        if current == None:
            print("List is empty")
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end="<-->")
            current = current.prev
        print("None")

    def insertatbeg(self,data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
    
    def insertatend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def insertatpos(self,data,pos):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        if pos==0:
            self.insertatbeg(data)
            return
        
        current = self.head
        count = 0
        while current and count<pos-1:
            current = current.next
            count += 1
        if current is None:
            print("Pos out of range")
            return 
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node


    def deleteatbeg(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def deleteatend(self):
        if self.head is None:
            print('List is empty')
            return
        if self.head.next is None:
            self.head = None
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None

    def deleteatpos(self,pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 0:
            self.deleteatbeg()
            return
        current = self.head
        count = 0
        while current and count<pos-1:
            current = current.next
            count += 1
        if current is None:
            print("Pos out of Range")
            return
        if current.next:
            current.next.prev = current.prev
            current.prev.next = current.next


N1 = DLL()
N1.insertatbeg(2)
N1.insertatbeg(1)
N1.insertatend(4)
N1.insertatend(5)
N1.insertatpos(3,2)

# N1.deleteatbeg()
# N1.deleteatend()
# N1.deleteatpos(2)
# 
print("")
N1.Traverse_Backward()
print("")
N1.Traverse_Forward()
