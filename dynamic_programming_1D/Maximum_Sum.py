'''
Maximum Sum

You are given an array A of N integers and three integers B, C, and D.
You have to find the maximum value of A[i]*B + A[j]*C + A[k]*D, where 1 <= i <= j <= k <= N.

Problem Constraints
1 <= N <= 10^5
-10000 <= A[i], B, C, D <= 10000

Example Input
Input 1:

 A = [1, 5, -3, 4, -2]
 B = 2
 C = 1
 D = -1
Input 2:

 A = [3, 2, 1]
 B = 1
 C = -10
 D = 3


Example Output
Output 1:

 18
Output 2:

 -4
'''
# maintain a dp arr for which we will compute max val after multiplying it by b or c or d
# initially we need to find the max value between dp[i] = max(b*a[i], dp[i-1])
# now we need to check which ind will give us max when multiplied by c 
# plus dp[i], so we will store dp[i] = max(c*a[i]+dp[i], dp[i-1])
# Now we need to do the same for d
class Solution:
    def solve(self, a, b, c, d):
        dp = [0]*len(a)
        dp[0] = b*a[0]
        for i in range(1,len(a)):
            dp[i] = max(b*a[i], dp[i-1])
            
        for i in range(1,len(a)):
            dp[i] = max(b*a[i], dp[i-1])
        dp[0] = dp[0] + a[0]*c    
        for i in range(1,len(a)):
            dp[i] = max(c*a[i]+dp[i], dp[i-1])
        
        dp[0] = dp[0] + a[0]*d   
        for i in range(1,len(a)):
            dp[i] = max(d*a[i]+dp[i], dp[i-1])
        return dp[-1]