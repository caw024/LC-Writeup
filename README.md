# LC-Writeup
Problem: Uncrossed Lines, https://leetcode.com/problems/uncrossed-lines/

# Approach: Top-Down Dynamic Programming

# Intuition:
Let ```A``` and ```B``` be our two integer arrays. Suppose we want to find the maximum number of uncrossed lines in the subarrays ```A[0...i]``` and ```B[0...j]``` (inclusive on both ends).

If the subarrays share the same last digit (```A[i] == B[j]```), then there exists a line connecting ```A[i]``` and ```B[j]```. Since ```A[i]``` and ```B[j]``` belong at the ends of the subarrays, this line connecting them won't intersect with any other lines. Therefore, we can draw in this line and look at the remaining subarrays ```A[0...i-1]``` and ```B[0...j-1]```.

Otherwise, the subarrays have different last digits (```A[i] != B[j]```). Then at least one of the ends of the subarrays does not belong to a line (If both of them had lines, they would intersect). This motivates us to look at the subarrays with one of the ends removed (```A[0...i-1], B[0...j]``` or ```A[0...i], B[0...j-1]```). Then, the answer is equal to whichever pair of subarrays generates the most uncrossed lines.

# Algorithm:
Let ```rec(i,j)``` be the function that computes the max number of uncrossed lines in the subarrays ```A[0...i]``` and ```B[0...j]```.

Base Case: 
When one or more of the subarrays are empty (when ``` i == -1``` or ``` j == -1```, then ```rec(i,j) = 0```). 

Recursive Step:
```
if A[i] == B[j]:
  rec(i,j) = rec(i-1,j-1) + 1
else:
  rec(i,j) = max( rec(i,j-1), rec(i-1,j) )
```

To save on runtime, create a map ```dp``` that maps the tuple ```(i,j)``` to ```rec(i,j)```. This lets us access previously computed values in ```O(1)``` time without having to repeatedly recompute the same results.

# Code:
See code.py

# Complexity Analysis
- Time Complexity: ```O(AB)``` since given  ```(i,j)``` is computed at most once. Computation takes ```O(1)``` but there are 
- Space Complexity: ```O(AB)``` since our map ```dp``` can stores each pair ```(i,j)``` with ```0 <= i < len(A)``` and ```0 <= j < len(B)```.
