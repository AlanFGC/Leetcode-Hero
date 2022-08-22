class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        # this is clearly a matrix problem where one output relies on the other
        # after trying bfs and other solutions. The pattern is really clear.
        # we need to progressively build up our solution by using our dp algorithm
        
        
        # declare a dp array
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        # this part is really tricky, if we don't have an initial value and a buffer this algorithm wouldn't work
        dp[0][1] = 1
        
        # because we are counting and not optimizing, this is a simple formula of dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    

        # we return the final output by calculating the very last space
        return dp[m][n]