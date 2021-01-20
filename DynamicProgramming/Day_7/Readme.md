# DAY 7 

## PROBLEMS : 

### Problem 1 : Bell Numbers

**Problem Statement :**
Given a set of n elements, find number of ways of partitioning it.

**Algorithm Type :** Dynamic Problem Algorithm

**Problem Complexity :** EASY

**Steps**
`
If j == 0
   // Then copy last entry of previous row
   // Note that i'th row has i entries
   Bell(i, j) = Bell(i-1, i-1) 

// If this is not first column of current row
Else 
   // Then this element is sum of previous element 
   // in current row and the element just above the
   // previous element
   Bell(i, j) = Bell(i-1, j-1) + Bell(i, j-1)
`

**Solution:**

```python3

```

**TimeComplexity :** O(n^2)


### Problem 1 : Catalan Numbers

**Problem Statement :**
Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems

The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862,


**Algorithm Type :** Dynamic Problem Algorithm

**Problem Complexity :** EASY

**Steps**
`
`

**Solution:**

```python3

```

**TimeComplexity :** O(nlogn)


### Problem 3 : Assign Unique Cap 

**Problem Statement :**

**Algorithm Type :** Dynamic Problem Algorithm

**Problem Complexity :** EASY

**Steps**
`
`

**Solution:**

```python3

```

**TimeComplexity :** O(nlogn)




