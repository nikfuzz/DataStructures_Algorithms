'''
Unique Binary Search Trees II

Given an integer A, how many structurally unique BST's (binary search trees) exist that can store values 1...A?

Problem Constraints
1 <= A <=18

Example Input
Input 1:

 1
Input 2:

 2


Example Output
Output 1:

 1
Output 2:

 2
'''
# We need to check with putting x elements on left and n-x on right
# this x can vary from 0 to n
# each of these values will result in a new combination of two sides (dp[n-x]*dp[x-1])
# Add the current dp[n] value to every combination
from math import factorial as fact
class Solution:
    def numTrees(self, a):
        # code for catlan number approach with O(a) time complexity
        '''
        count = 0
        n = 2*a
        count = fact(n)//(fact(a)*fact(n-a))
        count = count//(a+1)
        return count
        '''
        # code for dp approach 
        dp = [0 for i in range(a+1)]
        dp[1]=1
        dp[0]=1
        for i in range(2,a+1):
            for j in range(0,i+1):
                dp[i] = (dp[i-j]*dp[j-1]) + dp[i]
        return dp[-1]
# TC O(a^2)
# SC O(a)
        
