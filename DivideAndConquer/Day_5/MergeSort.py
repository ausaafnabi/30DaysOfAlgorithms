import random

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        # Dividing the array
        L = arr[:mid]
        R = arr[mid:]
        #Sorting the first half
        mergeSort(L)
        # Sorting the second half
        mergeSort(R)
        
        i = j = k = 0
        while i  < len(L) and j < len(R):
            if L[i] < R[i]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j +=1
            k +=1

        #Checking if any element is  left
        #merging
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    arr = []
    for i in range(random.randrange(300)):
        arr.append(random.randrange(100))
    print("Given Array is :: ", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted Array is :: ", end="\n")
    printList(arr)
