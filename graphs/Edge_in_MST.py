'''
Edge in MST

Given a undirected weighted graph with A nodes labelled from 1 to A with M edges given in a form of 2D-matrix B of size M * 3 where B[i][0] and B[i][1] denotes the two nodes connected by an edge of weight B[i][2].
For each edge check whether it belongs to any of the possible minimum spanning tree or not , return 1 if it belongs else return 0.
Return an one-dimensional binary array of size M denoting answer for each edge.
NOTE:
The graph may be disconnected in that case consider mst for each component.
No self-loops and no multiple edges present.
Answers in output array must be in order with the input array B output[i] must denote the answer of edge B[i][0] to B[i][1].

Problem Constraints
1 <= A, M <= 3*10^5
1 <= B[i][0], B[i][1] <= A
1 <= B[i][1] <= 10^3

Example Input
Input 1:

 A = 3
 B = [ [1, 2, 2]
       [1, 3, 2]
       [2, 3, 3]
     ]


Example Output
Output 1:

 [1, 1, 0]
'''

# Using Kruskal algorithm
# After sorting, consider every edge of weight w, if we can include it in our MST or not
# Then union the parents of the edges
# After unioning we move on to the next weight in the sorted order
import sys
sys.setrecursionlimit(10**6)

class Graph:
    def __init__(self, n):
        self.graph = []
        self.parent = [i for i in range(n+1)]
        self.size = [1 for i in range(n+1)]
        
    def addEdge(self, e, v, w, i):
        self.graph.append([e,v,w,i])
        
    def findSet(self, v):
        if v == self.parent[v]:
            return v
        self.parent[v] = self.findSet(self.parent[v])
        return self.parent[v]
        
    def unionSet(self, u, v):
        if self.size[v] < self.size[u]:
            v, u = u, v
        self.parent[u] = v
        self.size[v] += self.size[u]
            
    def Kruskal(self, a):
        ans = [0]*(len(self.graph))
        self.graph = sorted(self.graph, key = lambda x: x[2])
        i = 0
        j = 0
        e = 0
        while e != a-1 and i < len(self.graph):
            u,v,w,ind = self.graph[i]
            j = i
            while j < len(self.graph) and w == self.graph[j][2]:
                u,v,w,ind = self.graph[j]
                if self.findSet(u) != self.findSet(v):
                    ans[ind] = 1
                j += 1
            j = i
            while j < len(self.graph) and w == self.graph[j][2]:
                u,v,w,ind = self.graph[j]
                pu = self.findSet(u)
                pv = self.findSet(v)
                if pv != pu:
                    e += 1
                    self.unionSet(pu,pv)
                j += 1
            i = j
        return ans
            
        

class Solution:
    def solve(self, a, b):
        gr = Graph(a)
        for i in range(len(b)):
            gr.addEdge(b[i][0],b[i][1],b[i][2],i)
        ans = gr.Kruskal(a)
        return ans
# TC O(V + E * log E)
# SC O(E)