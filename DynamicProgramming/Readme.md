# Dynamic Programming

## Overview:
Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming.

The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later. This simple optimization reduces time complexities from exponential to polynomial.
## Concepts Related TO DP:

**Overlapping Subproblems:**
Like Divide and Conquer, Dynamic Programming combines solutions to sub-problems. Dynamic Programming is mainly used when solutions of same subproblems are needed again and again. In dynamic programming, computed solutions to subproblems are stored in a table so that these don’t have to be recomputed. So Dynamic Programming is not useful when there are no common (overlapping) subproblems because there is no point storing the solutions if they are not needed again.

**Optimal Substructure :**
A given problems has Optimal Substructure Property if optimal solution of the given problem can be obtained by using optimal solutions of its subproblems.

For example, the Shortest Path problem has following optimal substructure property:
If a node x lies in the shortest path from a source node u to destination node v then the shortest path from u to v is combination of shortest path from u to x and shortest path from x to v.

**Tabulation**-Bottom Up Dynamic Programming 
If state for our DP problem to be dp[x] with dp[0] as base state and dp[n] as our destination state. So,  we need to find the value of destination state i.e dp[n].
If we start our transition from our base state i.e dp[0] and follow our state transition relation to reach our destination state dp[n], we call it Bottom Up approach as it is quite clear that we started our transition from the bottom base state and reached the top most desired state.

**Memoisation**– Top Down Dynamic Programming
If we need to find the value for some state say dp[n] and instead of starting from the base state that i.e dp[0] we ask our answer from the states that can reach the destination state dp[n] following the state transition relation, then it is the top-down fashion of DP.

Here, we start our journey from the top most destination state and compute its answer by taking in count the values of states that can reach the destination state, till we reach the bottom most base state. 

## Steps To Solve a DP :
`
Steps to solve a DP
1) Identify if it is a DP problem
2) Decide a state expression with 
   least parameters
3) Formulate state relationship    
4) Do tabulation (or add memoization)

`
**Step 1 : How to classify a problem as a Dynamic Programming Problem?**
- Typically, all the problems that require to maximize or minimize certain quantity or counting problems that say to count the arrangements under certain condition or certain probability problems can be solved by using Dynamic Programming.
- All dynamic programming problems satisfy the overlapping subproblems property and most of the classic dynamic problems also satisfy the optimal substructure property. Once, we observe these properties in a given problem, be sure that it can be solved using DP.

**Step 2 : Deciding the state**

DP problems are all about state and their transition. This is the most basic step which must be done very carefully because the state transition depends on the choice of state definition you make. So, let’s see what do we mean by the term “state”.

**State** A state can be defined as the set of parameters that can uniquely identify a certain position or standing in the given problem. This set of parameters should be as small as possible to reduce state space.

**Step 3 : Formulating a relation among the states** 
This part is the hardest part of for solving a DP problem and requires a lot of intuition, observation, and practice.
Let’s think dynamically about this problem. So, first of all, we decide a state for the given problem. We will take a parameter n to decide state as it can uniquely identify any subproblem. So, our state dp will look like state(n).

**Step 4 : Adding memoization or tabulation for the state**
This is the easiest part of a dynamic programming solution. We just need to store the state answer so that next time that state is required, we can directly use it from our memory

## Problems :

Hmm... So, enough of the theory. Lets pull ourselves on the Problems and try to think of the solutions for some of the solution:

