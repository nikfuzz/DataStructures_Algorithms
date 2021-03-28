'''
Search in a row wise and column wise sorted matrix

Given a matrix of integers A of size N x M and an integer B.
In the given matrix every row and column is sorted in increasing order. Find and return the position of B in the matrix in the given form:
If A[i][j] = B then return (i * 1009 + j)
If B is not present return -1.

Note 1: Rows are numbered from top to bottom and columns are numbered from left to right.
Note 2: If there are multiple B in A then return the smallest value of i*1009 +j such that A[i][j]=B.

constraints:
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
-100000 <= B <= 100000

input:
A = [ [1, 2, 3]
          [4, 5, 6]
          [7, 8, 9] ]
B = 2

output:
1011
'''
def solve(a, b):
    n = len(a)
    m = len(a[0])
    
    i = 0
    j = m-1
    
    # if a row's last ele is smaller than b then we skip it.
    # if we find a row which has an ele greater than b then we search till j >= 0
    while i < n and j>=0:
        if a[i][j] == b:
            # traverse through duplicates
            while j >= 1:
                if a[i][j-1] != b:
                    break
                j -= 1
            return ((i+1)*1009 +(j+1))
        
        if a[i][j] > b:
            j -= 1
        
        else:
            i += 1
        
    return -1