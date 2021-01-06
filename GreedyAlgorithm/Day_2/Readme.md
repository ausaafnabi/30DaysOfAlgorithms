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


