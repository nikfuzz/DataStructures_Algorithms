'''
Dijsktra

Given a weighted undirected graph having A nodes and M weighted edges, and a source node C.
You have to find an integer array D of size A such that:
=> D[i] : Shortest distance form the C node to node i.
=> If node i is not reachable from C then -1.
Note:
There are no self-loops in the graph.
No multiple edges between two pair of vertices.
The graph may or may not be connected.
Nodes are numbered from 0 to A-1.
Your solution will run on multiple testcases. If you are using global variables make sure to clear them.

Problem Constraints
1 <= A <= 1e5
0 <= B[i][0],B[i][1] < A
0 <= B[i][2] <= 1e3
0 <= C < A


Example Input
Input 1:

A = 6
B = [   [0, 4, 9]
        [3, 4, 6] 
        [1, 2, 1] 
        [2, 5, 1] 
        [2, 4, 5] 
        [0, 3, 7] 
        [0, 1, 1] 
        [4, 5, 7] 
        [0, 5, 1] ] 
C = 4
Input 2:

A = 5
B = [   [0, 3, 4]
        [2, 3, 3] 
        [0, 1, 9] 
        [3, 4, 10] 
        [1, 3, 8]  ] 
C = 4


Example Output
Output 1:

D = [7, 6, 5, 6, 0, 6]
Output 2:

D = [14, 18, 13, 10, 0]
'''

# BFS
# maintain a min heap which will return the least distant neighbour from all the visited nodes
# At each node add its neighbour in the heap
# Until the heap is empty we pop the smallest distant element and add its unvisited neighbours in the heap
# For every node visited we add its cost in path array
import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vis = set()
        
    def add_node(self,e,v,w):
        self.graph[e].append((v,w))
        
    def dijstra(self, s, a):
        h = []
        heapq.heappush(h,(0,s))
        path = [99999]*a
        while h:
            w,v = heapq.heappop(h)
            self.vis.add(v)
            path[v] = min(w,path[v])
            for nv,nw in self.graph[v]:
                if nv not in self.vis:
                    heapq.heappush(h, (w+nw,nv))
        return path
        
class Solution:
    def solve(self, a, b, c):
        gr = Graph()
        for i in range(len(b)):
            gr.add_node(b[i][0],b[i][1],b[i][2])
            gr.add_node(b[i][1],b[i][0],b[i][2])
        ans = gr.dijstra(c,a)
        for i in range(len(ans)):
            if ans[i] == 99999:
                ans[i] = -1
        return ans
# TC O(v + e * log e), where v = vertices, e = edges
# SC O(v + e)
