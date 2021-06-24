'''
Floyd Warshall Algorithm

Given a matrix of integers A of size N x N, where A[i][j] represents the weight of directed edge from i to j (i ---> j).
If i == j, A[i][j] = 0, and if there is no directed edge from vertex i to vertex j, A[i][j] = -1.
Return a matrix B of size N x N where B[i][j] = shortest path from vertex i to vertex j.
If there is no possible path from vertex i to vertex j , B[i][j] = -1
Note: Rows are numbered from top to bottom and columns are numbered from left to right.

Problem Constraints
1 <= N <= 200
-1 <= A[i][j] <= 1000000

Example Input
A = [ [0 , 50 , 39]
          [-1 , 0 , 1]
          [-1 , 10 , 0] ]

Example Output
[ [0 , 49 , 39 ]
   [-1 , 0 , -1 ]
   [-1 , 10 , 0 ] ]
'''

# Consider each node as the intermediate node, k
# We need to check if the direct path from x node to y node is greater or smaller than x to k and k to y
# if the intermediate path is less costly then we should change a[i][j] value to x->k + k->y
class Solution:
    def solve(self, a):
        inf = float('inf')

        # replace -1 with inf for calculations
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == -1:
                    a[i][j] = inf
        # actual algorithm    
        for k in range(len(a)):
            for i in range(len(a)):
                for j in range(len(a)):
                    if a[i][k] + a[k][j] < a[i][j]:
                        a[i][j] = a[i][k] + a[k][j]

        # change inf back to -1 for desired output
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == inf:
                    a[i][j] = -1
        return a
# TC O(v^3), number of vertices
# SC O(1) auxilary space