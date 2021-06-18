'''
First Depth First Search

You are given N towns (1 to N). All towns are connected via unique directed path as mentioned in the input.
Given 2 towns find whether you can reach the first town from the second without repeating any edge.
B C : query to find whether B is reachable from C.
Input contains an integer array A of size N and 2 integers B and C ( 1 <= B, C <= N ).
There exist a directed edge from A[i] to i+1 for every 1 <= i < N. Also, it's guaranteed that A[i] <= i.
NOTE: Array A is 0-indexed.

Problem Constraints
1 <= n <= 100000

Example Input
Input 1:

 A = [1, 1, 2]
 B = 1
 C = 2
Input 2:

 A = [1, 1, 2]
 B = 2
 C = 1


Example Output
Output 1:

 0
Output 2:

 1
'''
# create an adjacency list for all the nodes in the graph
# create a visited set to check for visited elements
# do a dfs search from c until we find b or till all the nodes are visited
from collections import defaultdict

class Graph:
    def __init__(self):
       self.graph = defaultdict(list)
       self.vis = set()
       self.found = 0
       
    def addEdge(self, u, v):
        self.graph[u].append(v)
       
    def dfs(self, v, target):
        if v == target:
            self.found = 1
        self.vis.add(v)
        for u in self.graph[v]:
            if u not in self.vis:
                self.dfs(u,target)
        return 0
        

class Solution:
    def solve(self, a, b, c):
        gr = Graph()
        for i in range(len(a)):
            gr.addEdge(a[i],i+1)
        gr.dfs(c,b)
        return gr.found
# TC O(n)
# SC O(n)