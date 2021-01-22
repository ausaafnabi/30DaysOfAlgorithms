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
def bellNumber(n):
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1,n+1):
        #Explicitly fill for j =0
        bell[i][0] = bell[i-1][i-1]

        # Fill for remaining values
        for j in range(1,i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]

    return bell[n][0]


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
- make a table to store results of the subproblem
- Initialize first 2 variables in the table
- Fill the entries in the Table Using Recusive Formula
- Return the last entry
`

**Solution:**

```python3
def catalan(n): 
    if (n == 0 or n == 1): 
        return 1
  
    # Table to store results of subproblems 
    catalan = [0 for i in range(n + 1)] 
  
    # Initialize first two values in table 
    catalan[0] = 1
    catalan[1] = 1
  
    # Fill entries in catalan[]  
    # using recursive formula 
    for i in range(2, n + 1): 
        catalan[i] = 0
        for j in range(i): 
            catalan[i] += catalan[j]  
            catalan[i] *= catalan[i-j-1] 
  
    # Return last entry 
    return catalan[n] 
```

**TimeComplexity :** O(n)


### Problem 3 : Assign Unique Cap 

**Problem Statement :**
There are 100 different types of caps each having a unique id from 1 to 100. Also, there are ‘n’ persons each having a collection of a variable number of caps. One day all of these persons decide to go in a party wearing a cap but to look unique they decided that none of them will wear the same type of cap. So, count the total number of arrangements or ways such that none of them is wearing the same type of cap.

**Algorithm Type :** Dynamic Problem Algorithm

**Problem Complexity :** HARD 

**Steps**
`
Let i be the current cap number (caps from 1 to i-1 are already 
processed). Let integer variable mask indicates that the persons w
earing and not wearing caps.  If i'th bit is set in mask, then 
i'th person is wearing a cap, else not.

             // consider the case when ith cap is not included 
                     // in the arrangement
countWays(mask, i) = countWays(mask, i+1) +             
                    
                    // when ith cap is included in the arrangement
                    // so, assign this cap to all possible persons 
                    // one by one and recur for remaining persons.
                    ∑ countWays(mask | (1 << j), i+1)
                       for every person j that can wear cap i 
 
Note that the expression "mask | (1 << j)" sets j'th bit in mask.
And a person can wear cap i if it is there in the person's cap list
provided as input.

`

**Solution:**

```python3
def countWaysUtil(self,dp, mask, cap_no): 
        if mask == self.allmask: 
            return 1
  
        if cap_no > self.total_caps: 
            return 0
  
        if dp[mask][cap_no]!= -1 : 
            return dp[mask][cap_no] 
  
        ways = self.countWaysUtil(dp, mask, cap_no + 1) 
        if cap_no in self.caps: 
            for ppl in self.caps[cap_no]: 
                if mask & (1 << ppl) : continue
                ways += self.countWaysUtil(dp, mask | (1 << ppl), cap_no + 1)  
                ways = ways % (10**9 + 7) 
        dp[mask][cap_no] = ways 
        return dp[mask][cap_no] 
```

**TimeComplexity :** O(nlogn)




