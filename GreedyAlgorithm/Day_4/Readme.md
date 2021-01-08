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
1. Create a priorityQueue and insert all lengths into the Priority Queue.
2. Do following while the number of elements in Priority Queue is not one. 
   - Extract the minimum and second minimum from Priority Queue
   - Add the above two extracted values and insert the added value to the Priority Queue.
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
1. Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty.
2. Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first.
3. While sptSet doesn’t include all vertices
  - Pick a vertex u which is not there in sptSet and has minimum distance value.
  - Include u to sptSet.
  - Update distance value of all adjacent vertices of u.
`

**Solution:**

```python3
#Function to implement Dijkstra
def dijkstra(self,src):
    dist = [maxint] * self.V
    dist[src] = 0
    sptSet = [False]* self.V

    for count in range(self.V):
        # Pick the minimum distance vertex
        # from unprocessed vertices
        u = self.minDistance(dist ,sptSet)
        sptSet[u] = True
        # Update dist value of the adj vertices
        # only if curr >  new dist and c not in SPT
        for v in range(self.V):
            if self.graph[u][v] > 0 and sptSet[v] == False and \
            dist[v] > dist[u] + self.graph[u][v]:
                dist[v] = dist[u] + self.graph[u][v]

    self.printSolution(dist)
```

**TimeComplexity :** O(V^2), where V  are vertex.


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


