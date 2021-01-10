# DAY 5 

## PROBLEMS : 

### Problem 1 : MergeSort

**Problem Statement :**
Sort an array in nlogn complexity

**Algorithm Type :** Divide and Conquer Algorithm

**Problem Complexity :** EASY

**Steps**
`
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
`

**Solution:**

```python3
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        # Dividing the array
        L = arr[:mid]
        R = arr[mid:]
        #Sorting the first and second half
        mergeSort(L); mergeSort(R)
        
        i = j = k = 0
        while i  < len(L) and j < len(R):
            if L[i] < R[i]:
                arr[k] = L[i]; i += 1
            else:
                arr[k] = R[j]; j +=1
            k +=1

        #Checking if any element is  left
        #merging
        while i < len(L):
            arr[k] = L[i]
            i += 1; k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1; k += 1

```
**TimeComplexity :** O(nlogn)


### Problem 2 : Strassen Matrix Multiplication Problem

**Problem Statement :**


**Algorithm Type :** Divide and Conquer Algorithm

**Problem Complexity :** MEDIUM

**Solution:**
```python3
```
**TimeComplexity :** O(nlogn)


### Problem 3 : Coolie-Turkey FFT

**Problem Statement :**


**Algorithm Type :** Divide and Conquer Algorithm

**Problem Complexity :** HARD

**Solution:**

```python3
```
**TimeComplexity :** O(nlogn)




