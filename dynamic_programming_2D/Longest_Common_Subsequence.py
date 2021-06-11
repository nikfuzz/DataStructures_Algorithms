'''
Longest Common Subsequence

Given two strings A and B. Find the longest common subsequence ( A sequence which does not need to be contiguous), which is common in both the strings.
You need to return the length of such longest common subsequence.

Problem Constraints
1 <= Length of A, B <= 1005

Example Input
Input 1:

 A = "abbcdgf"
 B = "bbadcgf"
Input 2:

 A = "aaaaaa"
 B = "ababab"


Example Output
Output 1:

 5
Output 2:

 3
'''
# imagine two pointers: 1 on len(a)-1 and 1 on len(b)-1
# we compare the last chars of both strings
# if they are equal then we add one and move to second last in both strings
# else we take max for i-1,j or j-1,i (move either first pointer or second)
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def lcsFinder(self, a, b, i, j, dp):
        if i<0 or j<0:
            return 0
        if dp[i][j]: 
            return dp[i][j]
        elif a[i] == b[j]:
            dp[i][j] = 1 + self.lcsFinder(a,b,i-1,j-1,dp)
        else:
            dp[i][j] = max(self.lcsFinder(a,b,i-1,j,dp), self.lcsFinder(a,b,i,j-1,dp))
        return dp[i][j]
    
    def solve(self, a, b):
        dp = [[0 for i in range(len(a) + 1)] for j in range(0, len(b))]
        ans = self.lcsFinder(a,b, len(a)-1,len(b)-1,dp)
        return ans
# TC O(n*m), lengths of a and b
# SC O(n*m)