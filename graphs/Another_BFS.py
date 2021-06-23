'''
Another BFS

Given a weighted undirected graph having A nodes, a source node C and destination node D.
Find the shortest distance from C to D and if it is impossible to reach node D from C then return -1.
You are expected to do it in Time Complexity of O(A + M).
Note:
There are no self-loops in the graph.
No multiple edges between two pair of vertices.
The graph may or may not be connected.
Nodes are Numbered from 0 to A-1.
Your solution will run on multiple testcases. If you are using global variables make sure to clear them.

Problem Constraints
1 <= A <= 10^5
0 <= B[i][0], B[i][1] < A
1 <= B[i][2] <= 2
0 <= C < A
0 <= D < A

Example Input
Input 1:

 
A = 6
B = [   [2, 5, 1]
        [1, 3, 1] 
        [0, 5, 2] 
        [0, 2, 2] 
        [1, 4, 1] 
        [0, 1, 1] ] 
C = 3
D = 2
Input 2:

A = 2
B = [   [0, 1, 1]
    ] 
C = 0
D = 1


Example Output
Output 1:

 4
Output 2:

 1
'''
# Use Dijsktra's algorithm to find the shortest path for all nodes from source
# If you find the destination node then return its weight else return -1 when the heap becomes empty
import heapq as heap
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vis = set()
        
    def add_node(self,e,v,w):
        self.graph[e].append((v,w))
        
    def pathExists(self,s,d):
        h = []
        heap.heappush(h,(0,s))
        while h:
            w,v = heap.heappop(h)
            if v == d:
                return w
            self.vis.add(v)
            for nv,nw in self.graph[v]:
                if (nv not in self.vis):
                    heap.heappush(h,(nw+w,nv))
        return -1
        
class Solution:
    def solve(self, a, b, c, d):
        gr = Graph()
        for i in range(len(b)):
            gr.add_node(b[i][0],b[i][1],b[i][2])
            gr.add_node(b[i][1],b[i][0],b[i][2])
        return gr.pathExists(c,d)
# TC O(v + e * log e), v is vertices and e is edges
# SC O(v + e)