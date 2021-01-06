# DAY 2 

## PROBLEMS : 

### Problem 1 : Minimum Coins Problem

**Problem Statement :**
Consider there is need to change N amount of money, and have infinite supply of the each denominations of the currency.
What would be the minimum number of coins and/or notes needed to make the change?

**Algorithm Type :** Greedy Algorithm

**Problem Complexity :** EASY

**Steps :**
`
  - Sort the array of coins in decreasing order.
  - Initialize result as empty.
  - Find the largest denomination that is smaller than current amount.
  - Add found denomination to result. Subtract value of found denomination from amount.
  - If amount becomes 0, then print result.
  - Else repeat steps 3 and 4 for new value of V.
`

**Solution:**

```python3
def minCoins(currency):
  num = len(currency.deno)
  changeOfValue = []

  #Traversing through all deno
  i = num-1
  while(i>=0):
    while(currency.value >= currency.deno[i]):
      currency.value -= currency.deno[i]
      changeOfValue.append(currency.deno[i])
      i -=1

  return changeOfValue 

```
**TimeComplexity :** O(nlogn)


### Problem 2 : Fractional Knapsack Problem

**Problem Statement :**
Given weights and values of N items, Put Items in a knapsack of capacity W to get the maximum total value in the knapsack.

**Algorithm Type :** Greedy Algorithm

**Problem Complexity :** Medium

**Steps :**
`
  - Sort Items on basis of ratio.
  - Initialize total value as empty.
  - loop through all items.
  - if added Item won't overflow, add them.
  - elseif current Item overflows, add fraction of the item.
  - return totalValue
`

**Solution:**

```python3
def getMaxValue(wt,val,capacity):
    '''function to get maximum value'''
    iVal = []
    for i in range(len(wt)):
        iVal.append(ItemValue(wt[i],val[i],i))
    
    #sort in reverse by value
    iVal.sort(reverse=True)

    totalVal = 0
    for i in iVal:
        curWt = int(i.wt)
        curVal = int(i.val)
        if capacity - curWt >= 0:
            capacity -= curWt
            totalVal += curVal
        else:
            fraction = capacity/curWt
            totalVal += curVal * fraction
            capacity = int(capacity - (curWt*fraction))
            break
    return totalVal 
```
**TimeComplexity :** O(nlogn)


### Problem 3 : Job Sequencing Problem

**Problem Statement :**
Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline.
Maximize total profit if only one job can be scheduled at a time.


**Algorithm Type :** Greedy Algorithm

**Problem Complexity :** Medium

**Steps :**
`
- Sort all jobs in decreasing order of profit. 
- Iterate on jobs in decreasing order of profit.For each job , do the following : 
  - Find a time slot i, such that slot is empty and i < deadline and i is greatest. Put the job in this slot and mark this slot filled. 
  - If no such i exists, then ignore the job.
`

**Solution:**

```python3
def JobScheduling(jobs,t):
    n = len(jobs)

    # Sort all jobs acc. to
    # Decreasing order of the Profit
    #
    jobs.sort(reverse=True)

    result = [False] * t

    jobSq = ['-1'] * t

    for i in range(n):
        #Find a free slot for this job
        # (Start from last possible slot)
        for j in range(min(t-1,jobs[i].deadline-1),-1,-1):
            if result[j] is False:
                result[j] = True
                jobSq[j] = jobs[i].jobID 
                break
    return jobSq 
```
**TimeComplexity :** O(n^2)



