'''
Edit Distance

Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Problem Constraints
1 <= length(A), length(B) <= 450

Example Input
Input 1:

 A = "abad"
 B = "abac"
Input 2:

 A = "Anshuman"
 B = "Antihuman


Example Output
Output 1:

 1
Output 2:

 2
'''
# if a[i] == b[j] then we check the number of ways to change a[0 to i-1] to b[0 to j-1]
# else we take the 1 + min of replace, insert, and delete(in order as code) on string a
# dp[len(a)-1][len(b)-1] will give the final answer
class Solution:
    def minEdit(self, a, b, i, j, dp):
        if i<0: return j+1
        if j<0: return i+1
        if dp[i][j]:
            return dp[i][j]
        if a[i] == b[j]:
            dp[i][j] = self.minEdit(a,b,i-1,j-1,dp)
        else:
            dp[i][j] = 1 + min(self.minEdit(a,b,i-1,j-1,dp), self.minEdit(a,b,i,j-1,dp), self.minEdit(a,b,i-1,j,dp))
        return dp[i][j]
        
    def minDistance(self, a, b):
        dp = [[None for i in range(len(b))] for j in range(0, len(a))]
        self.minEdit(a, b, len(a)-1, len(b)-1, dp)
        ans = dp[-1][-1]
        return ans
# TC O(n*m), length of string a and b
# SC O(n*m)