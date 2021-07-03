'''
Distance of nearest cell

Given a matrix of integers A of size N x M consisting of 0 or 1.
For each cell of the matrix find the distance of nearest 1 in the matrix.
Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.
Find and return a matrix B of size N x M which defines for each cell in A distance of nearest 1 in the matrix A.
NOTE: There is atleast one 1 is present in the matrix.

Problem Constraints
1 <= N, M <= 1000
0 <= A[i][j] <= 1

Example Input
Input 1:

 A = [
       [0, 0, 0, 1]
       [0, 0, 1, 1] 
       [0, 1, 1, 0]
     ]
Input 2:

 A = [
       [1, 0, 0]
       [0, 0, 0]
       [0, 0, 0]  
     ]


Example Output
Output 1:

 [ 
   [3, 2, 1, 0]
   [2, 1, 0, 0]
   [1, 0, 0, 1]   
 ]
Output 2:

 [
   [0, 1, 2]
   [1, 2, 3]
   [2, 3, 4] 
 ]
'''
# Start BFS from nodes that have value 1
# Add coord for these nodes with d=0 as (x,y,d)
# Pop a node
# Keep adding adjacent nodes in queue and assign them distance d+1, d being the distance of the root of those nodes
# Then pop new node and repeat last step
from collections import deque

class Solution:
    def solve(self, a):
        vis = set()
        q = deque()
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == 1:
                    q.append((i,j,0))
                    vis.add((i,j))
                    a[i][j] = 0
        while q:
            x,y,d = q.popleft()
            dx = [0,0,-1,1]
            dy = [-1,1,0,0]
            for i in range(4):
                nx = dx[i]+x
                ny = dy[i]+y
                if nx >= 0 and nx < len(a) and ny >= 0 and ny < len(a[0]) and (nx,ny) not in vis:
                    a[nx][ny] = d+1
                    q.append((nx,ny,d+1))
                    vis.add((nx,ny))
        return a
# TC O(n*m), dimentions of the matrix
# SC O(n*m)