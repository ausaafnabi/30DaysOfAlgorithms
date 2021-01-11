# DAY 6 

## PROBLEMS : 

### Problem 1 : Quick Sort

**Problem Statement :**
Sort an array in nlogn complexity

**Algorithm Type :** Divide and Conquer Algorithm

**Problem Complexity :** EASY

**Steps**
`
Quick Sort(arr,low,high) 
  1. if low is less than high
  2. then, partition the array into two (can use high as pivot)
  3. For values < pivot and values > pivot
  4. Recursively Sort the partition using  Quick Sort
    - QuickSort(arr, low,partition-1)
    - QuickSort(arr, pi+1 , high)
`

**Solution:**

```python3
def quickSort(arr,low,high):
    if low<high:
        # pi is partition index
        pi = partition(arr,low,high)
        
        # Seperately Sort the elements
        # before and after partition
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

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
```

**TimeComplexity :** O(nlogn)


### Problem 2 : Quick Sort

**Problem Statement :**

**Algorithm Type :** Divide and Conquer Algorithm

**Problem Complexity :** MEDIUM

**Steps**
`
`

**Solution:**

```python3
```

**TimeComplexity :** O(nlogn)


### Problem 3 : Quick Sort

**Problem Statement :**

**Algorithm Type :** Divide and Conquer Algorithm

**Problem Complexity :** HARD

**Steps**
`
`

**Solution:**

```python3
```

**TimeComplexity :** O(nlogn)


