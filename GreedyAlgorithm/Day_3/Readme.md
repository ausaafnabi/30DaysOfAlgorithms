# DAY 2 

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

```
**TimeComplexity :** O(nlogn)


### Problem 2 : 

**Problem Statement :**

**Algorithm Type :** Greedy Algorithm

**Problem Complexity :** Medium

**Steps :**
`
`

**Solution:**

```python3
```
**TimeComplexity :** O(nlogn)


### Problem 3 : 

**Problem Statement :**


**Algorithm Type :** Greedy Algorithm

**Problem Complexity :** Medium

**Steps :**
`
`

**Solution:**

```python3
```
**TimeComplexity :** O(n^2)


