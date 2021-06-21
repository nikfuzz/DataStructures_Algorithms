'''
Number of islands

Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island. From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a corner with (i, j) and value in that cell is 1.

More formally, from any cell (i, j) if A[i][j] = 1 you can visit:
(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
(i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
(i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
(i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
(i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
Return the number of islands.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.

Problem Constraints
1 <= N, M <= 100
0 <= A[i] <= 1

Example Input
Input 1:

 A = [ 
       [0, 1, 0]
       [0, 0, 1]
       [1, 0, 0]
     ]
Input 2:

 A = [   
       [1, 1, 0, 0, 0]
       [0, 1, 0, 0, 0]
       [1, 0, 0, 1, 1]
       [0, 0, 0, 0, 0]
       [1, 0, 1, 0, 1]    
     ]


Example Output
Output 1:

 2
Output 2:

 5
'''
# each island is like a connected component
# at each i,j we try to find 1s that may be connected to the block
# Then we check all the 8 positions, if they are in matrix, visited, and has a '1'
# we call dfs on the safe spot among those 8 positions
# if there is no safe position to call dfs on then we are at the end of a cc and we inc 1 to the count
import sys
sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self, a):
        self.graph = a
        self.r = len(a)
        self.c = len(a[0])
        self.vis = [[False for j in range(self.c)] for i in range(self.r)]
    
    # to check if the next position is safe to call dfs on
    def isSafe(self, i,j):
        if (i>=0 and i<self.r) and (j>=0 and j<self.c) and (self.vis[i][j]==False) and (self.graph[i][j]==1):
            return True
        else:
            return False
        
        
    def dfs(self,i,j):
        # combination of all 8 positions possible from i,j
        row_itr = [-1,1,-1,-1,0,0,1,1]
        col_itr = [-1,1,0,1,-1,1,-1,0]
        
        self.vis[i][j] = True
        
        for k in range(8):
            if self.isSafe(i+row_itr[k], j+col_itr[k]):
                self.dfs(i+row_itr[k], j+col_itr[k])
                
    def countIslands(self):
        count = 0
        
        for i in range(self.r):
            for j in range(self.c):
                if self.vis[i][j] == False and self.graph[i][j] == 1:
                    self.dfs(i,j)
                    count += 1
        return count

class Solution:
    def solve(self, a):
        gr = Graph(a)
        return gr.countIslands()
# TC O(n*m)
# SC O(n*m)