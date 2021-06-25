'''
Commutable Islands

There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.
We need to find bridges with minimal cost such that all islands are connected.
It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.

Problem Constraints
1 <= A, M <= 6*10^4
1 <= B[i][0], B[i][1] <= A
1 <= B[i][2] <= 10^3

Example Input
Input 1:

 A = 4
 B = [  [1, 2, 1]
        [2, 3, 4]
        [1, 4, 3]
        [4, 3, 2]
        [1, 3, 10]  ]
Input 2:

 A = 4
 B = [  [1, 2, 1]
        [2, 3, 2]
        [3, 4, 4]
        [1, 4, 3]   ]


Example Output
Output 1:

 6
Output 2:

 6
'''
# Similar to Dijsktra
# maintain a min heap which will return min edge from current node
# start from any node and greedily keep visiting the min edge from each node
# keep a visited set to avoid visiting same element
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
            gr.addEdge(b[i][0],b[i][1],b[i][2])
            gr.addEdge(b[i][1],b[i][0],b[i][2])
        return gr.minSpTree(1)
# TC O(v + e * log e)
# SC O(v + e)