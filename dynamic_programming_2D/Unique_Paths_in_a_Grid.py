'''
Unique Paths in a Grid

Given a grid of size n * m, lets assume you are starting at (1,1) and your goal is to reach (n, m). 
At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).
Now consider if some obstacles are added to the grids. How many unique paths would there be? 
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Problem Constraints
1 <= n, m <= 100
A[i][j] = 0 or 1

Example Input
Input 1:

 A = [
        [0, 0, 0]
        [0, 1, 0]
        [0, 0, 0]
     ]
Input 2:

 A = [
        [0, 0, 0]
        [1, 1, 1]
        [0, 0, 0]
     ]


Example Output
Output 1:

 2
Output 2:

 0
'''
# to reach i,j cell we can come from i-1,j or i,j-1.
# We need to add the number of ways to reach i-1,j and i,j-1 to find unique paths at i,j
# if a[i][j] == 1, obstacle, then there are 0 ways to reach there
# save the unique no of paths till i,j in an arr dp[i][j]
# return dp[-1][-1] for the last cell, destination
class Solution:
    def calPaths(self, a, dp):
        # if starting is an obstacle then we cannot reach a[n][m]
        if a[0][0] == 1:
            return 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == 1:
                    dp[i][j] = 0
                # we can reach start in 1 way
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i-1][j] if i-1>=0 else 0) + (dp[i][j-1] if j-1>=0 else 0)
        return dp[-1][-1]
        
    def uniquePathsWithObstacles(self, a):
        dp = [[0]*len(a[0])]*len(a)
        ans = self.calPaths(a,dp)
        return ans
# TC O(n * m), dimensions of given matrix
# SC O(n * m)