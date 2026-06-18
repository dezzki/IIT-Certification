class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Single_CLL:
    def  __init__(self):
        self.head = None

    def Insertatend(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def Traverse(self):
        if self.head is None:
            print("List is empty")
            return
        Current = self.head
        while True:
            print(Current.data, end="-->")
            Current = Current.next
            if Current == self.head:
                break
        print("(Back to Head)")

    def Deletion(self,key): #Key = Data of the required node
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head
                
        #Case 1: Only 1 node in list
        if current.data == key and current.next == self.head:
            self.head = None
            return
        
        #Case 2: Deleting the head node, but more than 1 node exists
        if current.data == key: 
            #Find last node to update its next pointer
            tail = self.head
            while tail.next != self.head:
                tail = tail.next

            tail.next = self.head.next #Last node now points to 2nd node
            self.head = self.head.next 
            
        #Case 3: Deleting a non head node.
        
        

N1 = Single_CLL()
N1.Insertatend(1)
N1.Insertatend(2)

N1.Traverse()