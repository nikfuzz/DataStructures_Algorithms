'''
Max Sum Without Adjacent Elements

Given a 2 x N grid of integer, A, choose numbers such that the sum of the numbers is maximum and 
no two chosen numbers are adjacent horizontally, vertically or diagonally, and return it.
Note: You can choose more than 2 numbers.

Problem Constraints
1 <= N <= 20000
1 <= A[i] <= 2000

Example Input
Input 1:

 A = [   
        [1]
        [2]    
     ]
Input 2:

 A = [   
        [1, 2, 3, 4]
        [2, 3, 4, 5]    
     ]


Example Output
Output 1:

 2
Output 2:

 8
'''
# first make an array which has max((a[0][i], a[1][i])) since we want to maximize our result and choosing either of them
# eliminates the same possibilities
# then for every value in our max arr, we can either choose max at arr[i-1] or 
# we can choose the current element and max till arr[i-2]
# To avoid recomputation for max till i-2 and i-1 we keep storing the max till ith point in an arr called dp
class Solution:
    def adjacent(self, a):
        max_a = []
        for i in range(len(a[0])):
            max_a.append(max(a[0][i], a[1][i]))
        dp = []
        if len(max_a) == 1:
            return max_a[0]
        if len(max_a) >= 2:
            dp.append(max_a[0])
            dp.append(max(max_a[0], max_a[1]))
            
        for i in range(2,len(max_a)):
            dp.append(max((dp[i-2]+max_a[i]),dp[i-1]))
        return dp[-1]
# TC O(n)
# SC O(n)
