'''
Let's Party

In Danceland, one person can party either alone or can pair up with another person.
Can you find in how many ways they can party if there are A people in Danceland?
Note: Return your answer modulo 10003, as the answer can be large.

Problem Constraints
1 <= A <= 10^5

Example Input
Input 1:

 A = 3
Input 2:

 A = 5


Example Output
Output 1:

 4
Output 2:

 26
'''

class Solution:
    # The recursive code:
    '''
    # def waysToParty(self, n, dp):
    #     if dp[n]:
    #         return dp[n]%10003
    #     dp[n] = self.waysToParty(n-1, dp)%10003 + (((n-1)%10003)*self.waysToParty(n-2, dp)%10003)%10003
    #     return dp[n]
    '''
    # Each person can party alone or they can pair up with n-1 people
    # When partying alone, no of ways to party will be ways(n-1)
    # When partying in a pair, you can pair with n-1 people + ways(n-2)
    def solve(self, n):
        if n == 1:
            return n
        dp = [None]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1]%10003 + (((i-1)%10003)*(dp[i-2]%10003))%10003
            
        return dp[n]%10003
# TC O(n)
# SC O(n)