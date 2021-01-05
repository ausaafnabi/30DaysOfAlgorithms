# Day 1

## Overview

Today, Let's cover the greedy algorithms. More specifically a few popular greedy algorithms.

------------------------------------
Greedy approach is all about short term benefits. In more academic terms :

> Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. Greedy algorithms are used for optimization problems. An optimization problem can be solved using Greedy if the problem has the following property: At every step, we can make a choice that looks best at the moment, and we get the optimal solution of the complete problem.

Now just because it gives immediate benefits does'nt mean that it is always good. Why? 🤔 

Because sometimes greedy algorithm is unable to find the global maximum of the problem which makes sense, as NP-Hard Problems like Travelling Salesman Problem has convergence issues sometimes.


## Problems

Hmm... So, enough of the theory. Lets pull ourselves on the Problems and try to think of the solutions for these:

### Problem 1 : Activity Selection Problem

**Problem Statement :**
Given n activities with their start and finish times. 
Assuming, worker is working on single activity at a time, select the maximum number of activities that can be performed by a single person.

**Algorithm Type :** Greedy Algorithm

**Solution:**

```python3
def ActivitySelection(activities):
  num = len(activities)
  # take i as the first activity
  i=0
  save(i)   # save first activity
  
  # consider the remaining activities
  for j in range(num)
    # if curr activity start time >= finish time of first activity
    # save activity and make curr to first
    if activities[j].start >= activities[i].finish:
      save(j)
      i = j 
  
```
**TimeComplexity :** O(nlogn)


### Problem 2 : Minimum Spanning Tree Problem

**Problem Statement :** 
A spanning tree of that graph is a subgraph that is a tree and connects all the vertices together.
A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected and undirected graph is a spanning tree with weight less than or equal to the weight of every other spanning tree. 

**Steps :**
```
1. Sort all the edges in non-decreasing order of their weight. 
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it. 
3. Repeat step#2 until there are (V-1) edges in the spanning tree.
```

**Algorithm Type :** Greedy Algorithm

**Solution :**
```python3
  # Function to construct MST using Kruskal's algorithms 
  def KruskalMST(graph,V):
    result = [] 
    i,e=0,0 
    
    # Sort all the edges in increasing order of their weight
    graph = sort(graph)

    parent = []
    rank = []
    
    # Create V subsets with single elements
    for node in range(V):
        parent.append(node)
        rank.append(0)
        
    # Number of edges to be taken is equal to V-1
    while e < V-1:
        #Pick smallest edge and move the iteration
        u,v,w = self.graph[i]
        i = i+1
        x = self.find(parent,u)
        y = self.find(parent,v)
        if x!=y:
            e = e+1
            result.append([u,v,w])
            self.union(parent,rank,x,y)
        
        minimumCost = 0
        print("Edges in the constructed MST")
        for u,v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u,v,weight))
        print("Minimum Spanning Tree", minimumCost)
```

**Time Complexity :** 
O(ElogE) or O(ElogV) ,where E and V are number of edges and Vertices respectively
Also, Find and Union operations can take almost  O(logV)
