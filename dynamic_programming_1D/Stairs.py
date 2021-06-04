'''
Stairs

You are climbing a stair case and it takes A steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Problem Constraints
1 <= A <= 36

Example Input
Input 1:

 A = 2
Input 2:

 A = 3


Example Output
Output 1:

 2
Output 2:

 3
'''
# You can either reach nth step from n-1th step or n-2th step.
# element of choice is i-1 and i-2
# waysToClimb(n) gives the number of ways to climb n steps
# Recurance relations is waysToClimb(i) = waysToClimb(i-1) + waysToClimb(i-2)
# Use a dp array to store the states already visited
class Solution:
    def waysToClimb(self, a, dp):
        if dp[a]:
            return dp[a]
        dp[a] = self.waysToClimb(a-1, dp) + self.waysToClimb(a-2, dp)
        return dp[a]
	
    def climbStairs(self, a):
        dp = [None]*(a+1)
        dp[1] = 1
        if a>1:
            dp[2] = 2
        return self.waysToClimb(a, dp)
