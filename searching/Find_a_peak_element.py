'''
Find a peak element

Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors.
For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.
NOTE: Users are expected to solve this in O(log(N)) time.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 109

Input 1:
A = [1, 2, 3, 4, 5]
Input 2:
A = [5, 17, 100, 11]

Output 1:
 5
Output 2:
 100
'''

class Solution:
    def solve(self, a):
        if len(a) == 1:
            return a[0]
        
        if len(a) == 2:
            return max(a)
        
        l = 0
        r = len(a)-1
        
        while(l<=r):
            m = (l+r)//2
            
            # if peak is at corner
            if m==0 and a[m]>a[m+1]:
                return a[m]
            
            if m == len(a)-1 and a[m]>a[m-1]:
                return a[m]
            
            # peak element condition
            if a[m] >= a[m-1] and a[m] >= a[m+1]:
                return a[m]
            
            if a[m]<a[m-1]:
                r = m - 1
            
            else:
                l = m + 1
        
        return -1