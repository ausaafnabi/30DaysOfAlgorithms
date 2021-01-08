# DAY 4 

## PROBLEMS : 

### Problem 1 : N Ropes Problem 

**Problem Statement :**
There are given n ropes of different lengths, we need to connect these ropes into one rope.
The cost to connect two ropes is equal to the sum of their lengths. Find a way to connect the ropes with minimum cost.

**Algorithm Type :** Greedy Algorithm

**Problem Complexity :** EASY

**Steps :**
`
1. Create a min-heap and insert all lengths into the min-heap.
2. Do following while the number of elements in min-heap is not one. 
   - Extract the minimum and second minimum from min-heap
   - Add the above two extracted values and insert the added value to the min-heap.
   - Maintain a variable for total cost and keep incrementing it by the sum of extracted values.
3. Return the value of this total cost.

`

**Solution:**

```python3
def minCost(ropes):
    # Create a priority Queue out of list
    heapq.heapify(ropes)

    #initialize result
    result = 0

    while(len(ropes) > 1):
        #Extract shortest of 2 ropes
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        # Connect the ropes : update the result
        # Insert a new rope
        result += first + second
        heapq.heappush(ropes,first+second)
    return result 
```

**TimeComplexity :** O(nlogn), 


### Problem 2 : Shortest Path Problem

**Problem Statement :**


**Algorithm Type :** Greedy Algorithm

**Problem Complexity :** Medium

**Steps :**
`
`

**Solution:**

```python3
```

**TimeComplexity :** O(V^2+E), where V and E are vertex and edges.


### Problem 3 : Minimum Spanning Tree  Problem

**Problem Statement :**

**Algorithm Type :** Greedy Algorithm

**Problem Complexity :** HARD 

**Steps :**
`
`
**Solution:**

```python3
```


**TimeComplexity :** O(n^2)


