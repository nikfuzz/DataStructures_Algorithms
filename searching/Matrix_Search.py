'''
Matrix Search

Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integar B in matrix A.
This matrix A has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.
NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.

Problem Constraints
1 <= N, M <= 1000
1 <= A[i][j], B <= 106

Example Input
Input 1:

A = [ 
      [1,   3,  5,  7]
      [10, 11, 16, 20]
      [23, 30, 34, 50]  
    ]
B = 3
Input 2:

A = [   
      [5, 17, 100, 111]
      [119, 120, 127, 131]    
    ]
B = 3


Example Output
Output 1:
1
Output 2:
0
'''

class Solution:
    # iterate i until you find a[i][m-1] >= b
    # This row could have the element we need
    # use binary search on the row
    def searchMatrix(self, a, b):
        n = len(a)
        m = len(a[0])
        
        for i in range(n):
            while a[i][m-1] < b:
                i += 1
                if i == n:
                    return 0
            
            l = 0
            r = m-1
            
            while(l<=r):
                m = (l+r) // 2
                if a[i][m] == b:
                    return 1
                if a[i][m] > b:
                    r = m-1
                else:
                    l =  m+1
                    
            return 0