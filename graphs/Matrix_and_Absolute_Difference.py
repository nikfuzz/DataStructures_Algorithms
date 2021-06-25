'''
Matrix and Absolute Difference

Given a matrix C of integers, of dimension A x B.
For any given K, you are not allowed to travel between cells that have an absolute difference greater than K.
Return the minimum value of K such that it is possible to travel between any pair of cells in the grid through a path of adjacent cells.

NOTE:
Adjacent cells are those cells that share a side with the current cell.

Problem Constraints
1 <= A, B <= 10^2
1 <= C[i][j] <= 10^9

Example Input
Input 1:

 A = 3
 B = 3
 C = [  [1, 5, 6]
        [10, 7, 2]
        [3, 6, 9]   ]


Example Output
Output 1:

 4
'''
# let all elements of the matrix be graph points on a graph
# The weights on the edges will be the 2 nodes' absolute difference
# Then apply prim's algorithm to calculate min spanning tree of the matrix
# take the max weighted edge from this MST as the ans
from collections import defaultdict
import heapq as heap

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vis = set()
        
    def addEdge(self, v, u, w):
            self.graph[v].append((u,w))
        
    def calMinK(self, s):
        h = []
        heap.heappush(h,(0,s))
        k = 0
        while h:
            w,v = heap.heappop(h)
            if v in self.vis:
                continue
            k = max(w,k)
            self.vis.add(v)
            for nv,nw in self.graph[v]:
                if nv not in self.vis:
                    heap.heappush(h,(nw,nv))
        return k
# TC O(v + e * log e)
# SC O(v + e)
        

class Solution:
    def solve(self, a, b, c):
        gr = Graph()
        for i in range(a):
            for j in range(b):
                if i>=1:
                    gr.addEdge((i-1)*b+j,(i)*b+j,abs(c[i-1][j]-c[i][j]))
                if i<a-1:
                    gr.addEdge((i+1)*b+j,(i)*b+j,abs(c[i+1][j]-c[i][j]))
                if j>=1:
                    gr.addEdge(i*b+(j-1),i*b+j,abs(c[i][j-1]-c[i][j]))
                if j<b-1:
                    gr.addEdge(i*b+(j+1),i*b+j,abs(c[i][j+1]-c[i][j]))
        return gr.calMinK(0)