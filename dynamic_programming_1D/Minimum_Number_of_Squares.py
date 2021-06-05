'''
Minimum Number of Squares

Given an integer A. Return minimum count of numbers, sum of whose squares is equal to A.

Problem Constraints
1 <= A <= 105

Example Input
Input 1:

 A = 6
Input 2:

 A = 5


Example Output
Output 1:

 3
Output 2:

 2
'''
# To find the min number of squares we need to run a loop to find k in i-k, k = sq of 1 to root(i)
# We need to find the min of dp[i] and dp[i-k]+1 
class Solution:
    def calMinSq(self, n):
        dp = [0,1,2,3]
        map = {}
        # storing the squares to avoid extra time complexity in calculating squares
        for i in range(1,n+1):
            if i not in map:
                map[i] = i*i
        for i in range(4, n+1):
            dp.append(i)
            for x in range(1,i):
                temp = map[x]
                if temp > i:
                    break
                else:
                    dp[i] = min(dp[i], dp[i-temp]+1)
        return dp[n]
	
    def countMinSquares(self, n):
        return self.calMinSq(n)
# TC O(n * root(n))
# SC O(n)