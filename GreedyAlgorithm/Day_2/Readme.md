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



