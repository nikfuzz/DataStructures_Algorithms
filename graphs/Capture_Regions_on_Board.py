'''
Capture Regions on Board

Given a 2-D board A of size N x M containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Problem Constraints
1 <= N, M <= 1000

Example Input
Input 1:

 A = [ 
       [X, X, X, X],
       [X, O, O, X],
       [X, X, O, X],
       [X, O, X, X] 
     ]
Input 2:

 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]


Example Output
Output 1:

 After running your function, the board should be:
 A = [
       [X, X, X, X],
       [X, X, X, X],
       [X, X, X, X],
       [X, O, X, X]
     ]
Output 2:

 After running your function, the board should be:
 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]
'''
# Iterate through the borders of the board
# If you find a O then run a dfs on the O indexes to find all the connected Os from it,
# if they are connected then those O will not be captured, so mark those O
# Finally convert all marked Os to O and the untouched Os will be captured and flipped to X
class Solution:
    def dfs(self, a, x, y):
        if a[x][y] != 'O':
            return
        a[x][y] = '#'
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        
        for i in range(4):
            if x+dx[i] >= 0 and x+dx[i] < len(a) and y+dy[i] >= 0 and y+dy[i] < len(a[0]):
                self.dfs(a, x+dx[i], y+dy[i])
                
    def solve(self, a):
        for i in range(len(a)):
            if a[i][0] == 'O':
                self.dfs(a,i,0)
                
            if a[i][len(a[0])-1] == 'O':
                self.dfs(a,i,len(a[0])-1)
                
        for j in range(len(a[0])):
            if a[0][j] == 'O':
                self.dfs(a,0,j)
            if a[len(a)-1][j] == 'O':
                self.dfs(a,len(a)-1,j)
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == '#':
                    a[i][j] = 'O'
                elif a[i][j] == 'O':
                    a[i][j] = 'X'
        return a
# TC O(n * m), dimentions of the board
# SC O(n * m), for the recursion stack