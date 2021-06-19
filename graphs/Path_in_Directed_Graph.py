'''
Path in Directed Graph

Given an directed graph having A nodes labelled from 1 to A containing M edges given by matrix B of size M x 2
such that there is a edge directed from node
B[i][0] to node B[i][1].
Find whether a path exists from node 1 to node A.
Return 1 if path exists else return 0.
NOTE:
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.

Problem Constraints
2 <= A <= 10^5
1 <= M <= min(200000,A*(A-1))
1 <= B[i][0], B[i][1] <= A

Example Input
Input 1:

 A = 5
 B = [  [1, 2] 
        [4, 1] 
        [2, 4] 
        [3, 4] 
        [5, 2] 
        [1, 3] ]
Input 2:

 A = 5
 B = [  [1, 2]
        [2, 3] 
        [3, 4] 
        [4, 5] ]


Example Output
Output 1:

 0
Output 2:

 1
'''
# make an adjacency list of the graph
# start from 1 and do a dfs until target(b) is found
import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vis = set()
        self.target_found = 0
        
    def add_node(self, u, v):
        self.graph[u].append(v)
        
    def search_dfs(self, v, target):
        if v == target:
            self.target_found = 1
        self.vis.add(v)
        for u in self.graph[v]:
            if u not in self.vis:
                self.search_dfs(u,target)
        return 0

class Solution:
    def solve(self, a, b):
        gr = Graph()
        for i in range(len(b)):
            gr.add_node(b[i][0], b[i][1])
        gr.search_dfs(1,a)
        return gr.target_found
# TC O(n)
# SC O(n)
