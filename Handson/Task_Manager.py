import heapq

class Task:
    def __init__(self,priority,name):
        self.priority = priority
        self.name = name
    
    def __repr__(self):
        return f"{self.name} (Priority : {self.priority})"
    
class TaskManager:
    def __init__(self):
        self.heap = []
    
    def add_task(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap)-1)

    def top_completed(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

    def _heapify_up(self,index):
        while index > 0:
            parent = (index - 1)//2 #Starts with 0

            if self.heap[index].priority < self.heap[parent].priority:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break
        
    def _heapify_down(self,index):
        size = len(self.heap)

        while True:
            left = 2*index+1
            right = 2*index+2
            smallest = index

            if left < size and self.heap[left]:
                pass