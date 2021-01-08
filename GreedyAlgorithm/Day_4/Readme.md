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
Given a graph and a source vertex in the graph, find shortest paths from source to all vertices in the given graph.
We'll use Dijkstra’s algorithm to find shortest path .In which, we generate a SPT (shortest path tree) with given source as root. We maintain two sets, one set contains vertices included in shortest path tree, other set includes vertices not yet included in shortest path tree. At every step of the algorithm, we find a vertex which is in the other set (set of not yet included) and has a minimum distance from the source.
 NOTE: if we use Adjecency List then we can decrease the complexity to O(ELogV). Also, Check Dial's algorithm which is a more efficient algorithm for SPT.
 
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
Using Prims Algorithm, find the MST of a given graph.
 
**Algorithm Type :** Greedy Algorithm

**Problem Complexity :** HARD 

**Steps :**
`
1. Create a Priority Queue of size V where V is the number of vertices in the given graph. Every node of min heap contains vertex number and key value of the vertex.
2. Initialize the first vertex as root (the key value assigned to first vertex is 0). The key value assigned to all other vertices is INF (infinite).
3. While Priority Queue is not empty, do following
  - Extract the min value node from Priority Queue. Let the extracted vertex be u.
  - For every adjacent vertex v of u, check if v is in Priority Queue (not yet included in MST). 
    - If v is in Priority Queue and its key value is more than weight of u-v, 
    - then update the key value of v as weight of u-v.
`

**Solution:**

```python3
def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst

```


**TimeComplexity :** O(VLogE), where V and E are vertices and edges respectively.



