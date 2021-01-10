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

Given two square matrices A and B of size n x n each, find their multiplication matrix.
> The idea of Strassen’s method is to reduce the number of recursive calls. Strassen’s method is similar to simple divide and conquer method except that it divides it into 4 sub matrices and eq using product addition

**Algorithm Type :** Divide and Conquer Algorithm

**Problem Complexity :** MEDIUM

**STEPS :**
`
Divide and Conquer method to multiply two square matrices.
- Divide matrices A and B in 4 sub-matrices of size N/2 x N/2.
- Compute recursively value of p1....pN-1; where 
- Calculate following values recursively for 4 quadrants.
    - p5+p4-p2+p6 
    - p1+p2
    - p3 + p4 
    - and p1 + p5 - p2 - p7. 
`

**Solution :**
```python3
def strassen(x,y):
    if len(x) == 1:
        return x*y
    
    a,b,c,d = split(x)
    e,f,g,h = split(y)

    # computing 7 products, recursively
    p1 = strassen(a,f-h)
    p2 = strassen(a+b,h)
    p3 = strassen(c+d,e)
    p4 = strassen(d,g-e)
    p5 = strassen(a+d,e+h)  
    p6 = strassen(b-d,g+h)
    p7 = strassen(a-c,e+f)

    # computing 4 quadrants
    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    # Combining 4 quadrants into single by stacking horizontally
    c = np.vstack((np.hstack((c11,c12)),np.hstack((c21,c22))))

    return c
```
**TimeComplexity :** O(n^log7)


### Problem 3 : Coolie-Turkey FFT

**Problem Statement :**


**Algorithm Type :** Divide and Conquer Algorithm

**Problem Complexity :** HARD


**Solution:**

```python3

```
**TimeComplexity :** O(nlogn)




