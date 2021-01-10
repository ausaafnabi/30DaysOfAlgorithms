# Divide And Conquer

## Overview:

As the name suggest this algorithm strategy focuses on Solving the problem by breaking it into smaller components.

`
The technique can be divided into 3 parts:
- **Divide:** This involves dividing the problem into some sub problem.
- **Conquer:** Sub problem by calling recursively until sub problem solved.
- **Combine:** The Sub problem Solved so that we will get find problem solution. 
`
> The divide-and-conquer technique is the basis of efficient algorithms for many problems, such as sorting (e.g., quicksort, merge sort), multiplying large numbers (e.g., the Karatsuba algorithm), finding the closest pair of points, syntactic analysis (e.g., top-down parsers), and computing the discrete Fourier transform (FFT).

## General Algorithm (STRUCTURE) :
`
DAC(a, i, j)
{
    if(endcondition)
      return(Solution(a, i, j))
    else 
      m = divide(a, i, j)               // f1(n)
      b = DAC(a, i, mid)                 // T(n/2)
      c = DAC(a, mid+1, j)            // T(n/2)
      d = combine(b, c)                 // f2(n)
   return(d)
}
`

## HOW DAC is different from DP ?

Both paradigms (D & C and DP) divide the given problem into subproblems and solve subproblems. Divide and Conquer should be used when same subproblems are not evaluated many times. Otherwise Dynamic Programming or Memoization should be used. For example, Binary Search is a Divide and Conquer algorithm, we never evaluate the same subproblems again. On the other hand, for calculating nth Fibonacci number, Dynamic Programming should be preferred

## Problems :

Hmm... So, enough of the theory. Lets pull ourselves on the Problems and try to think of the solutions for some of the solution:

### Day 5:

Problems in Solved in Day 5:

 - **Problem 1 : Merge Sort **

 - **Problem 2 : Strassen's Matrix Multiplication**

 - **Problem 3 : Coolie-Turkey FFT** 

**READ :** [Day 5 Complete Readme!](../Day_5/Readme.md "Day 5 Complete Reference")



