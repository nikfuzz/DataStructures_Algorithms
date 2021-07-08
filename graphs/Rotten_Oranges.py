'''
Rotten Oranges

Given a matrix of integers A of size N x M consisting of 0, 1 or 2.
Each cell can have three values:
The value 0 representing an empty cell.
The value 1 representing a fresh orange.
The value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten. 
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead.
Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.

Problem Constraints
1 <= N, M <= 1000
0 <= A[i][j] <= 2

Example Input
Input 1:

A = [   [2, 1, 1]
        [1, 1, 0]
        [0, 1, 1]   ]
Input 2:

 
A = [   [2, 1, 1]
        [0, 1, 1]
        [1, 0, 1]   ]

Example Output
Output 1:

 4
Output 2:

 -1
'''
# Run bfs from all nodes that have value 2
# Keep adding the visited nodes in a set
# The queue will have coord and distance from the initial 2(degree) which gives us the minutes
from collections import deque

class Solution:
    def solve(self, a):
        vis = set()
        q = deque()
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == 2:
                    q.append((i,j,0))
                    vis.add((i,j))
        ans = 0
        while q:
            x,y,d = q.popleft()
            ans = max(ans, d)
            dx = [0,0,-1,1]
            dy = [-1,1,0,0]
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx >= 0 and nx < len(a) and ny >= 0 and ny < len(a[0]) and (nx,ny) not in vis and a[nx][ny] == 1:
                    a[nx][ny] = 2
                    q.append((nx,ny,d+1))
                    vis.add((nx,ny))
                    
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == 1:
                    return -1
        return ans
# TC O(V + E), vertices and edges
# SC O(V), V = n*m