'''
Rotated Sorted Array Search

Given a sorted array of integers A of size N and an integer B.
array A is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).
You are given a target value B to search. If found in the array, return its index, otherwise return -1.
You may assume no duplicate exists in the array.
NOTE: Users are expected to solve this in O(log(N)) time.

Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 10^9
all elements in A are disitinct.

Input 1:
A = [4, 5, 6, 7, 0, 1, 2, 3]
B = 4

Input 2:
A = [1]
B = 1

Output 1:
 0
Output 2:
 0
'''

class Solution:
    # we try to find k in the inc slope
    # We check if the k lies in the range othrwise we modify the range
    def pivotS(self,a,l,r,k):
        if l>=r:
            return -1
        
        m = (l + r)//2
        
        if a[m] == k:
            return m
        elif a[m] >= a[l]:
            if k <= a[m] and k>= a[l]:
                return self.pivotS(a,l,m,k)
            else:
                return self.pivotS(a,m+1,r,k)
        else:
            if k <= a[r] and k>=a[m]:
                return self.pivotS(a,m,r,k)
            else:
                return self.pivotS(a,l,m-1,k)
    
    def search(self, a, b):
        p = self.pivotS(a,0,len(a)-1,b)
        return p