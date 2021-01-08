# DAY 3 

## PROBLEMS : 

### Problem 1 : Minimum Platform Problem 

**Problem Statement :**

Given arrival and departure times of all trains that reach a railway station, 
Find the minimum number of platforms required for the railway station so that no train waits.

**Algorithm Type :** Greedy Algorithm

**Problem Complexity :** EASY

**Steps :**
`

- Sort the arrival and departure time of trains.
- Initialize two pointers i=0, j=0 and a var to store ans and current count plat
- Loop while i<n and j<n 
  - Compare the ith element of arrival array and jth element of departure array.
  - If the arrival time <= departure then:
    - one more platform is needed so increase the count, i.e. plat++ and increment i
  - Else if the arrival time > departure then:
    - one less platform is needed so decrease the count, i.e. plat++ and increment j
- Update the ans, i.e ans = max(ans, plat).
`

**Solution:**

```python3
def findPlatform(Station):
    n = len(Station)
    Station.sort()
    plat_needed = 1
    result = 1
    i=1 
    j=0
    while(i<n and j<n):
        if (Station[i].arr<=Station[j].dep):
            plat_needed +=1
            i +=1
        elif(Station[i].arr > Station[j].dep):
            plat_needed -= 1
            j += 1
        
        if (plat_needed > result):
            result = plat_needed
    return result
```
**TimeComplexity :** O(nlogn)


### Problem 2 : Graph Coloring Problem

**Problem Statement :**
Given m colors, find a way of coloring the vertices of a graph such that no two adjacent vertices are colored using same color. 

NOTE: Graph Coloring is a NP-Complete Problem. Hence, There is no efficient Solution available. Approximate algorithms are used to solve it though. Greedy Algorithm gurantees that the upper bound is never more than d+1. where d is maximum degree of vertex 


**Algorithm Type :** Greedy Algorithm

**Problem Complexity :** Medium

**Steps :**
`
1. Color first vertex with first color.
2. Do following for remaining V-1 vertices.
  - Consider the currently picked vertex and color it with the
lowest numbered color that has not been used on any previously
colored vertices adjacent to it. 
  - If all previously used colors appear on vertices adjacent to v,
    - assign a new color to it.
`

**Solution:**

```python3
def colorGraph(graph,colors,N):
    # stores color assigned to each V
    result = {}
    
    # assign color to V one by one
    for u in range(N):
        # set to store color of adj vertices of u
        # check color of adj of u and store in set
        assigned = set([result.get(i) for i in graph.adj[u] if i in result])
        # check for the first free color
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1
        #assigns vertex u the first available color
        result[u] = color
    
    for v in range(N):
        print("Color assigned to vertex",v,"is",colors[result[v]])
```

**TimeComplexity :** O(V^2+E), where V and E are vertex and edges.


### Problem 3 : Minimize CashFlow Problem

**Problem Statement :**
Given a number of friends who have to give or take some amount of money from one another.
Find a solution to minimize the total cash flow among all the friends.

**Algorithm Type :** Greedy Algorithm

**Problem Complexity :** HARD 

**Steps :**
`
1) Compute the net amount for every person. The net amount for person ‘i’ can be computed be subtracting sum of all debts from sum of all credits.

2) Find the two persons that are maximum creditor and maximum debtor. Let the maximum amount to be credited maximum creditor be maxCredit and maximum amount to be debited from maximum debtor be maxDebit. Let the maximum debtor be Pd and maximum creditor be Pc.

3) Find the minimum of maxDebit and maxCredit. Let minimum of two be x. Debit ‘x’ from Pd and credit this amount to Pc

4) If x is equal to maxCredit, then remove Pc from set of persons and recur for remaining (n-1) persons.

5) If x is equal to maxDebit, then remove Pd from set of persons and recur for remaining (n-1) persons.
`


**TimeComplexity :** O(n^2)


