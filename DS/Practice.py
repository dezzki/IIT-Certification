#*Singli Linked List*


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



#*Doubli Linked List*


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def Travserse_Forward(self):
        current = self.head
        while current:
            print(current.data, end='<-->')
            current = current.next
        print('None')
    
    def Traverse_Backward(self):
        current = self.head
        if current is None:
            print("List is empty")
            return
        while current.next:
            current = current.next
        while current:
            print(current.data,end="<-->")
            current = current.prev
        print('None')

    def IAB(self,data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def IAE(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def IAP(self,data,pos):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        if pos == 0:
            self.IAB(data)
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

    def DAB(self):
        if self.head is None:
            print("List is empty")
            return
        
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def DAE(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None 

    def DAP(self,pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 0:
            self.IAB()
            return
        current = self.head
        count = 0
        while current and count < pos-1:
            current = current.next
            count += 1
            if current is None:
                print("Pos out of range")
                return
        current.prev.next = current.next
        current.next.prev = current.prev


N1 = DLL()
N1.IAB(5)
N1.IAB(4)
N1.IAB(3)
N1.IAB(2)
N1.IAB(1)

N1.IAE(6)
N1.IAE(7)
N1.IAE(8)

N1.IAP(0,3)

N1.DAP(4)

N1.DAB()
N1.DAE()

N1.Travserse_Forward()
N1.Traverse_Backward()