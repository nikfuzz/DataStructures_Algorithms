'''
Valid Binary Search Tree

Given a binary tree represented by root A.
Assume a BST is defined as follows:
1) The left subtree of a node contains only nodes with keys less than the node's key.
2) The right subtree of a node contains only nodes with keys greater than the node's key.
3) Both the left and right subtrees must also be binary search trees.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9

Example Input
Input 1:

 
   1
  /  \
 2    3
Input 2:

 
  2
 / \
1   3


Example Output
Output 1:

 0
Output 2:

 1
'''
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# Since we are using a fail first approach we will go for preorder traversal
# We need to set a min and max value for each subtree
# if the root.val is smaller than min or greater than max we return False
# new min is root.val-1 for left subtree and new max is root.val+1 for right subtree
class Solution:
    def isValidBSTUtil(self, root, mi, ma):
        if not root: return True
        if root.val < mi or root.val > ma:
            return False
        return (self.isValidBSTUtil(root.left, mi, root.val-1) and self.isValidBSTUtil(root.right, root.val+1, ma))
	
    def isValidBST(self, root):
        if self.isValidBSTUtil(root, float('-inf'), float('inf')):
            return 1
        else:
            return 0
# TC O(n)
# SC O(n)
