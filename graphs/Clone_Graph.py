'''
Clone Graph

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
Note: The test cases are generated in the following format (use the following format to use See Expected Output option):
First integer N is the number of nodes.
Then, N intgers follow denoting the label (or hash) of the N nodes.
Then, N2 integers following denoting the adjacency matrix of a graph, where Adj[i][j] = 1 denotes presence of an undirected edge between the ith and jth node, O otherwise.

Problem Constraints
1 <= Number of nodes <= 10^5

Example Input
Input 1:

      1
    / | \
   3  2  4
        / \
       5   6
Input 2:

      1
     / \
    3   4
   /   /|\
  2   5 7 6


Example Output
Output 1:

 Output will the same graph but with new pointers:
      1
    / | \
   3  2  4
        / \
       5   6
Output 2:

      1
     / \
    3   4
   /   /|\
  2   5 7 6
'''
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Info:
    def __init__(self):
        self.vis = {}

# Create a clone node for each given node
# Run a loop through its neighbors array and recursively call clone of its neighbour and append it 
# to the neighbour list of the original clone node
# In order to avoid any repeatition, we will store node->clone in a dict/hashmap
# If we have already visited a node then we will just return its clone
class Solution:
    def cloneGraphUtil(self, node, info):
        # If we touch a null node
        if node == None:
            return node
        if node in info.vis:
            return info.vis[node]
        clone = UndirectedGraphNode(node.label)
        info.vis[node] = clone
        for neighbour in node.neighbors:
            clone.neighbors.append(self.cloneGraphUtil(neighbour, info))
        return clone
    
    def cloneGraph(self, node):
        info = Info()
        return self.cloneGraphUtil(node, info)
# TC O(N), number of the nodes
# SC O(N + H), H = Height of the graph, due to the recursion stack.
        