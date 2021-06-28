'''
Construction Cost

Given a graph with A nodes and C weighted edges. Cost of constructing the graph is the sum of weights of all the edges in the graph.
Find the minimum cost of constructing the graph by selecting some given edges such that we can reach every other node from the 1st node.
NOTE: Return the answer modulo 109+7 as the answer can be large.

Problem Constraints
1 <= A <= 100000
0 <= C <= 100000
1 <= B[i][0], B[i][1] <= N
1 <= B[i][2] <= 109

Example Input
Input 1:

A = 3
B = [   [1, 2, 14]
        [2, 3, 7]
        [3, 1, 2]   ]
Input 2:

A = 3
B = [   [1, 2, 20]
        [2, 3, 17]  ]

Example Output
Output 1:

9
Output 2:

37
'''
# In order to get the min cost we need to make a MST from the given graph
# Use Prim's Algoritm to calculate total sum of all the paths in the mst
from collections import defaultdict
import heapq as heap

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vis = set()
        
    def addEdge(self, v, u, w):
        self.graph[v].append((u,w))
        
    def minSpTree(self,s):
        h = []
        heap.heappush(h,(0,s))
        totalSum = 0
        while h:
            w,v = heap.heappop(h)
            if v in self.vis:
                continue
            totalSum += w
            self.vis.add(v)
            for nv,nw in self.graph[v]:
                if nv not in self.vis:
                    heap.heappush(h,(nw,nv))
        return totalSum

class Solution:
    def solve(self, a, b):
        gr = Graph()
        for i in range(len(b)):
            gr.addEdge(b[i][0], b[i][1], b[i][2])
            gr.addEdge(b[i][1], b[i][0], b[i][2])
        return gr.minSpTree(1) % (10**9 + 7)
# O(v + e * log e)
# O(v + e)
