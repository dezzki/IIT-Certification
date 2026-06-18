class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.capacity
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow! No space")
            return
        self.queue.append(item)
        print(f"Enqueued : {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! No items")
            return
        removed = self.queue.pop(0)
        print(f"Dequeued : {removed}")
        return removed
    
    def display(self):
        if self.is_empty():
            print("Queue Underflow! No items")
            return
        
        print("\n ### QUEUE ### \n")
        for item in self.queue:
            print(item,end=" - ")
        print("(end)")
        print("")

q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.display()

q.dequeue()

q.display()