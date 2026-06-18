# #  **STACKS**

# # LIFO : Last In, First Out.
 
# # Functionality :
# # - PUSH : adds an item to the top of the stack.
# # - POP : removes the top item from the stack.
# # - PEEK/TOP : see whats at the top without removing it.
# # - IS_EMPTY : check if the stack is empty or not.

# class stack:
#     def __init__(self, capacity):
#         self.stack = [] #using list to store stack elements
#         self.capacity = capacity

#     def  is_empty(self): #Check if stack is empty.
#         return len(self.stack) == 0
    
#     def is_full(self):
#         return len(self.stack) == self.capacity
    
#     def push(self, item):
#         if self.is_full():
#             print(f"Stack Overflow! Can't add {item} to the stack")
#         else:
#             self.stack.append(item)
#             print(f"Pushed : {item}")

#     def pop(self):
#         if self.is_empty():
#             print("Stack Underflow! No item to pop")
#             return None
        
#         popped_item = self.stack.pop()
#         print(f"Popped : {popped_item}")
#         return popped_item
    
#     def peek(self):
#         if self.is_empty():
#             print("No elements to peek at")
#             return None
        
#         top_item = self.stack[-1]
#         print(f"Top Item : {top_item}")
#         return top_item
    
#     def display(self):
#         if self.is_empty():
#             print("Stack is empty, Stack Underflow, Nothing to Display.")
#             return None
#         else:
#             print("\n### STACK(Top to bottom) ###\n")
#             for item in reversed(self.stack):
#                 print(f"- {item}")
#             print('')


# S = stack(5)

# S.push("Vansh")
# S.push("Himadri")
# S.push("Rishi")
# S.push("Yogit")
# S.push("Sehej")
# S.push("Vishu")


# S.display()

# S.peek()
# S.pop()

# S.display()


class Stacks:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.capacity
    
    def push(self, item):
        if self.is_full():
            print("Stack Overflow, No space in stack")
            return
        
        self.stack.append(item)
        print(f"Pushed : {item}")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! No item to pop")
            return
        popped_item = self.stack.pop()
        print(f"Popped : {popped_item}")
        return popped_item
    
    def peek(self):
        if self.is_empty():
            print("Stack Underflow! No item to peek")
            return
        
        top_item = self.stack[-1]
        print(f"Top Item : {top_item}")
        return top_item
    
    def display(self):
        if self.is_empty():
            print("Stack Underflow! No item to display")
            return
        
        print("\n### STACK ###\n")
        for i in self.stack:
            print(f"- {i}")
        print("")

S = Stacks(5)
S.push(1)
S.push(2)
S.push(3)

S.pop()
S.peek()

S.display()