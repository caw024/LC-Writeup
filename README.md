# LC-Writeup
# Problem: Uncrossed Lines, https://leetcode.com/problems/uncrossed-lines/

# Approach: Top-Down Dynamic Programming

# Intuition:
Let A and B be our two integer arrays. Suppose we want to find the maximum number of uncrossed lines of the subarrays A[0...i] and B[0...j].

If the subarrays share the same last digit (A[i] == B[j]), then there exists a line connecting A[i] and B[j]. Because A[i] and B[j] belong at the same ends of the subarrays, the line connecting them won't intersect with any other lines. Then, we keep track of this line and look at the remaining subarrays A[0...i-1] and B[0...j-1].

Otherwise, the subarrays have different last digits (A[i] != B[j]) and there isn't such a line. Then our answer is max(A[0...i-1],B

# Algorithm:
Let the array dp[i][j] store the maximum number of uncrossed lines of subarrays A[0...i] and B[0...j]. 

If A[i] == B[j]:
  dp[i][j] = dp[i-1][j-1] + 1
Else:
  dp[i][j] = max(dp[i][j-1], dp[i-1][j])

Code:


# Complexity Analysis
Our array dp is of length 
- Time Complexity: O(AB) 
- Space Complexity: O(AB) since we store every combination of letters of A with letters of B
