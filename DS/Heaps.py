# Heap - 

class MinHeap:
    def __init__(self):
        self.heap=[]

    def insert(self,val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)

    def delete_min(self):
        if len(self.heap)==0:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return min_val
    
    def heapify_up(self,index):
        parent = (index-1)//2
        if index>0 and self.heap[index]<self.heap[parent]:
            self.heap[index],self.heap[parent] = self.heap[parent],self.heap[index]
            self.heapify_up(parent)

    def heapify_down(self,index):
        smallest = index
        left = 2*index+1
        right = 2*index+2

        if left<len(self.heap) and self.heap[left]<self.heap[smallest]:
            smallest = left
        if right<len(self.heap) and self.heap[right]<self.heap[smallest]:
            smallest = right
        if smallest!=index:
            self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
            self.heapify_down

    def display(self):
        print(self.heap)

heap = MinHeap()
list = list(range(10))

for i in list:
    heap.insert(i)

heap.display()

min_val = heap.delete_min()
print("deleted value:", min_val)

heap.display()



class Maxheap:
    def __init__(self):
        self.heap=[]

    def parent(self,index):
        return (index-1)//2
    
    def left_child(self,index):
        return 2*index+1
    
    def right_child(self,index):
        return 2*index+2
    
    def insert(self,val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self,index):
        if index>0 and self.heap[index]<self.heap[self.parent(index)]:
            self.heap[index],self.heap[self.parent(index)] = self.heap[self.parent(index)],self.heap[index]
            self.heapify_up(parent)