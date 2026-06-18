#Recursion

# A function that calls itself to solve smaller versions of a problem.
#You keep breaking the problem until you reach a base case(end condition).


#count down timer

def countdown(n):
    if n == 0:
        print("Time's Up!")
    else:
        print(n)
        countdown(n-1) #function call
# countdown(15)


# Factorial 

def fact(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    return n*fact(n-1)

# print(fact(5))


# Linear search 

# going through each item one by one untill you find the item.
# principle -> doing something one by one.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"Target found at index value : {i}")
            return i
    return "Target not in list"

arr1 = [1,2,3,4,5,6,7,8]

# print(linear_search(arr1,6))


#binary search

# -search a sorted list by cutting it in half
# -Faster than linear search
# -Divide and conquer
# -O(log n)

def binary_search(arr,target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == target:
            print(f'Value found!! at {mid}')
            return mid
        elif arr[mid]<target:
            low = mid+1
        elif arr[mid] > target:
            high = mid-1

    print("value not found!!")
    return -1

# binary_search(arr1,3)



# Sorting Algorithms

data = [2,4,3,55,7,1]



#Bubble sort ->
#repeatedly compares adjacent elements and swaps them if they are in the wrong order.

#Ascending 
def bubble_sort(arr):
    n = len(arr) #No of elements in array

    print(n)

    for i in range(n): #Controls how many times we repeast comparing and swapping
        for j in range(0,n-i-1): #comparing adjacent elements
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j] # swapping
    return arr

# print(bubble_sort(data))

#decending
def bubble_sort(arr):
    n = len(arr) #No of elements in array

    print(n)

    for i in range(n): #Controls how many times we repeast comparing and swapping
        for j in range(0,n-i-1): #comparing adjacent elements
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j] # swapping
    return arr

# print(bubble_sort(data))





#Selection sort :

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        MinVal = i

        for j in range(i+1,n): #starts comparing after i
            if arr[j] < arr[MinVal]:
                MinVal=j

        arr[i],arr[MinVal] = arr[MinVal], arr[i]

    return arr

sorted_data = selection_sort(data)

# print(f"Selection reeturned {sorted_data}")





#Insertion sort:

#simple algorithm that build hte final dorted array one item at a time 


def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        key = arr[i] #current element
        j = i-1 #holds previous value of arr[i]

        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        
        arr[j+1] = key

    print(f"insertion sorted data {arr}")

insertion_sort(data)