data = [1,2,3,4,5,6,7,8]
data2 = [4,3,2,6,1,44,6]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"Linear found target at index value: {i}")
            return i
    print("Target not found")

# linear_search(data,4)


def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            print(f"Binary found target at index {mid}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[arr] > target:
            high = mid-1

    print("Target not found")

# binary_search(data,7)


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            print(f"current value of i is {i}")
            print(f"current value of j is {j}\n")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# print(bubble_sort(data2))


def selection_sort(arr):
    print(arr,"\n")

    n = len(arr)

    for i in range(n):
        MinVal = i

        for j in range(i+1,n):
            print(f"current value of i is {i},    {arr[i]}")
            print(f"current value of j is {j},    {arr[j]}")

            if arr[j] < arr[MinVal]:
                MinVal = j
                print(arr,"\n")
        arr[i],arr[MinVal] = arr[MinVal], arr[i]
        print(arr,"\n")

    
    return arr

# print(selection_sort(data2))


def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        print(f"Value of i is : {i},    {arr[i]}")
        print(f"Value of j is : {j}     {arr[j]}")

        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            print(arr)
            print(f"Value of j is : {j}     {arr[j]}")

        arr[j+1] = key
        print(arr,"\n")

print(insertion_sort(data2))