class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        # dp is a set that stores previous values of rec(i,j) for memoization
        dp = collections.defaultdict(int)
        
        # let rec(i,j) denotes maximum num of uncrossed lines of subarray A[0...i] and B[0...j]
        def rec(i,j):
            nonlocal A,B,dp

            # Base case: empty subarray reached
            if i == -1 or j == -1:
                dp[(i,j)] = 0
                return 0

            # access a previously computed value if available
            if (i,j) in dp:
                return dp[(i,j)]

            # the recursive step
            if A[i] == B[j]:
                dp[(i,j)] = 1 + rec(i-1,j-1)
                return dp[(i,j)]
            else:
                dp[(i,j)] = max(rec(i-1,j), rec(i,j-1))
                return dp[(i,j)]
        
        return rec(len(A)-1,len(B)-1)
