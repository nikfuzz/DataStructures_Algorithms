'''
Kth Smallest Element In Tree

Given a binary search tree represented by root A, write a function to find the Bth smallest element in the tree.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9

Example Input
Input 1:

 
            2
          /   \
         1    3
B = 2
Input 2:

 
            3
           /
          2
         /
        1
B = 1



Example Output
Output 1:

 2
Output 2:

 1
'''

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# counter class to count k smallest elements
class Counter:
    def __init__(self):
        self.i = 0
    def inc(self):
        self.i += 1
    def getCounter(self):
        return self.i

# The inorder traversal gives us node values in a sorted order
# We make a counter class to count the number of nodes we traverse in inorder fashion
# If the left becomes null we inc the counter
# We keep inc counter for nodes in the left sub tree, until counter, i == k
class Solution:
    def getKthSmallest(self, root,k,i):
        if not root:
            return None
        left = self.getKthSmallest(root.left, k,i)
        if left != None:
            return left
        i.inc()
        if i.getCounter() == k:
            return root.val
        return self.getKthSmallest(root.right, k,i)
	
	
    def kthsmallest(self, root, k):
        i = Counter()
        ans = self.getKthSmallest(root,k,i)
        return ans
# TC O(n)
# SC O(h), height of the tree
