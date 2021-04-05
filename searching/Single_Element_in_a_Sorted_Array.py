'''
Single Element in a Sorted Array

Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.
NOTE: Users are expected to solve this in O(log(N)) time.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9

Input 1:
A = [1, 1, 7]

Input 2:
A = [2, 3, 3]

Output 1:
 7
Output 2:
 2
'''

class Solution:
    # the second occ of a number occurs on even pos before the req element and after it, the pos is odd
    # we check if pos is even or odd and modify the search span accordingly
    def binS(self,a,st,end):
        
        if st > end:
            return None
        
        if st == end:
            return a[st]
            
        mid = (st + end)//2
        
        if mid & 1 == 0:
            if a[mid] == a[mid+1]:
                return self.binS(a,mid+2, end)
            else:
                return self.binS(a,st,mid)
        
        if mid & 1 == 1:
            if a[mid] == a[mid-1]:
                return self.binS(a,mid+1,end)
            else:
                return self.binS(a,st,mid-1)
    
    def solve(self, a):
        return self.binS(a,0,len(a)-1)