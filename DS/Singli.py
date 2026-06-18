class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linked_List:
    def __init__(self):
        self.head = None

    def Traverse(self):
        current = self.head
        while current:
            print(f"{current.data} ->",end=" ")
            current = current.next
        print('None')

    def insertatbeg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertatend(self,data):
        if self.head == None:
            self.insertatbeg(data)
            return
                
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.next = None

    def insertatpos(self,data,pos):
        if pos == 0:
            self.insertatbeg(data)
            return
        
        new_node = Node(data)
        current = self.head
        count = 0
        while current and count<pos-1:
            count += 1
            current = current.next
            if current == None:
                print('Pos out of Range')
                return
        new_node.next = current.next
        current.next = new_node

    def removeaatbeg(self):
        if self.head == None:
            print("Empty linked list")
            return
        
        current = self.head
        current = current.next
        self.head = current

    def removeatend(self):
        if self.head == None:
            print("List is Empty")
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def removeatpos(self,pos):
        if pos == 0:
            print("Pos out of Range")
            return
        if pos == 1:
            self.removeaatbeg()
            return
        count = 0
        current = self.head
        while current and count<pos-1:
            current = current.next
            count += 1
            if current == None:
                print("pos out of range")
                return
        current.next = current.next.next


N1 = Linked_List()
N1.insertatend(10)
N1.insertatbeg(2)
N1.insertatbeg(1)
N1.insertatend(11)
N1.insertatpos(3,2)
N1.insertatpos(4,3)
N1.insertatend(99)

N1.removeatpos(4)
N1.removeatend()
N1.removeaatbeg()
N1.Traverse()