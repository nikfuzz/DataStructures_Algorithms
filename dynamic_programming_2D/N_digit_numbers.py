'''
N digit numbers

Find out the number of A digit positive numbers, whose digits on being added equals to a given number B.
Note that a valid number starts from digits 1-9 except the number 0 itself. i.e. leading zeroes are not allowed.
Since the answer can be large, output answer modulo 1000000007

Problem Constraints
1 <= A <= 1000
1 <= B <= 10000

Example Input
Input 1:

 A = 2
 B = 4
Input 2:

 A = 1
 B = 3


Example Output
Output 1:

 4
Output 2:

 1
'''
# We need to find no of ways to create sum s-i(i=0 to 10) from 1 to a digits
# store the sum in a dp[x][y] arr where x = value of a and y = value of sum
# Taking the sum of the number of ways will give the final answer
class Solution:
    def calSum(self, dp, id, s):
        if s<0: return 0
        if id == 0 and s == 0: return 1
        if id == 0: return 0
        
        if dp[id][s] != None:
            return dp[id][s]
        ans = 0
        for i in range(10):
            ans += self.calSum(dp,id-1, s-i)
            ans %= 1000000007
        dp[id][s] = ans
        return dp[id][s]
	
    def solve(self, a, b):
        if a == 1 and b<10:
            return 1
        dp = [[None for j in range(b+1)] for i in range(a+1)]
        ans = 0
        for i in range(1,10):
            ans += self.calSum(dp,a-1,b-i)
            ans %= 1000000007
        return ans
# TC O(a*b)
# SC O(a*b)