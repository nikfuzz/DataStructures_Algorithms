'''
Identical Binary Trees

Given two binary trees, check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

Problem Constraints
1 <= number of nodes <= 105

Example Input
Input 1:

   1       1
  / \     / \
 2   3   2   3
Input 2:

   1       1
  / \     / \
 2   3   3   3


Example Output
Output 1:

 1
Output 2:

 0
'''

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# compare root1.val and root2.val and left subtree and right subtree
# if all are true return true
class Solution:
    def isSameTree(self, root1, root2):
        # if we reach the end
        if not root1 and not root2:
            return 1
        # if one of the subtree runs out of nodes and other one does not
        if not root1 or not root2:
            return 0
        if (root1.val == root2.val and self.isSameTree(root1.left,root2.left) and self.isSameTree(root1.right,root2.right)):
            return 1
        else:
            return 0
        
        
        
        