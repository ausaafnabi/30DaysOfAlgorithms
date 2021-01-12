import random

# Function to do partition
# Takes last element as pivot element
# places the element at correct position
# and places all smaller in left and 
# larger elements in right of pivot
def partition(arr,low,high):
    i = low-1
    pivot = arr[high]

    for j in range(low,high):
        # if Current ele is smaller than pivot
        if arr[j] < pivot:
            # increment the index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

# Recursive function to call QuickSort
def quickSort(arr,low,high):
    if low<high:
        # pi is partition index
        pi = partition(arr,low,high)
        
        # Seperately Sort the elements
        # before and after partition
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

#Driver Code
if __name__ == "__main__":
    arr = []
    for i in range(100000):#random.randrange(200)):
        arr.append(random.randrange(123112))
    n = len(arr)
    print("Array :: ")
    print(arr)
    quickSort(arr,0,n-1)
    print("Sorted Array is:")
    print(arr)
