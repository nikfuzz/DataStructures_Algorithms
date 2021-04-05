'''
Sorted Insert Position

Given a sorted array A of size N and a target value B, return the index (0-based indexing) if the target is found.
If not, return the index where it would be if it were inserted in order.
NOTE: You may assume no duplicates in the array. Users are expected to solve this in O(log(N)) time.

Problem Constraints
1 <= N <= 106

Input 1:
A = [1, 3, 5, 6]
B = 5

Input 2:
A = [1]
B = 1

Output 1:
2
Output 2:
0
'''
class Solution:
    def searchInsert(self, a, b):
        
        l = 0
        r = len(a)-1
        # for corner elements
        if a[r] < b:
            return r + 1
        
        if a[l] > b:
            return l
        
        # first look if the element is present
        while(l<=r):
            m = (l + r)//2
            if a[m] == b:
                return m
            elif a[m] > b:
                r = m-1
            else:
                l = m+1
        
        l = 0
        r = len(a)-1
        # if it is not present we look for its apparant position
        while(l<=r):
            m = (l+r)//2
            
            if a[m-1] < b and a[m] > b:
                return m
            
            elif a[m-1]< b and a[m]<b:
                l = m+1
            else:
                r = m-1
        
        return -1
        