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


### Problem 2 : Karatsuba Fast Multiplication

**Problem Statement :**
Given 2 numbers, Multiply the two numbers faster than n^2 complexity

**Algorithm Type :** Divide and Conquer Algorithm

**Problem Complexity :** MEDIUM

**Steps**
`
procedure karatsuba(num1, num2)
    if (num1 < 10) or (num2 < 10)
        return num1 × num2
    
    /* Calculates the size of the numbers. */
    m = min(size_base10(num1), size_base10(num2))
    m2 = floor(m / 2) 
    /* m2 = ceil(m / 2) will also work */
    
    /* Split the digit sequences in the middle. */
    high1, low1 = split_at(num1, m2)
    high2, low2 = split_at(num2, m2)
    
    /* 3 calls made to numbers approximately half the size. */
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)
    
    return (z2 × 10 ^ (m2 × 2)) + ((z1 - z2 - z0) × 10 ^ m2) + z0
`

**Solution:**

```python3
def karatsuba(x,y):
    '''Function to multiply 2 numbers in a more efficient manner'''
    if len(str(x)) == 1 or len(str(y)) ==1:
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        nby = n//2
        # extracting 1 and second halves of both
        a = x // 10**(nby)
        b = x % 10**(nby)
        c = y // 10**(nby)
        d = y % 10**(nby)

        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        ad_plus_bc = karatsuba(a+b,c+d) - ac - bd

        # writing n as 2*nby takes care of both even and odd n
        #
        prod = ac * 10**(2*nby) + (ad_plus_bc * 10**nby) + bd
    
    return prod
```

**TimeComplexity :** O(n^log3)


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


