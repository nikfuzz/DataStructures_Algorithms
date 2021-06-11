'''
Min Sum Path in Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
Adjacent numbers for jth number of row i is jth and (j+1)th numbers of row i+1

Problem Constraints
|A| <= 1000
A[i] <= 1000

Example Input
Input 1:

 
A = [ 
         [2],
        [3, 4],
       [6, 5, 7],
      [4, 1, 8, 3]
    ]
Input 2:

 A = [ [1] ]


Example Output
Output 1:

 11
Output 2:

 1
'''
# We have two choices for each a[i][j], either to add a[i][j-1] or add a[i][j]
# make a dp arr which will store min sum till i,j based on above condition
# min(dp[len(a)-1]), i.e, the last row, will give us the answer
class Solution:
    def minimumTotal(self, a):
        dp = []
        for i in range(len(a)):
            dp.append([])
            for j in range(len(a[i])):
                dp[i].append(0)
        dp[0][0] = a[0][0]
        for i in range(1,len(dp)):
            for j in range(len(dp[i])):
                if j==len(dp[i])-1:
                    dp[i][j] = (dp[i-1][j-1] + a[i][j])
                elif j == 0:
                    dp[i][j] = (dp[i-1][j] + a[i][j])
                else:
                    dp[i][j] = (min(dp[i-1][j], dp[i-1][j-1]) + a[i][j])
        return min(dp[-1])
# TC O(N), where N is number of elements in the triangle
# SC O(N)