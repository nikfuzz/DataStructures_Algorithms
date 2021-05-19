'''
Min Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
 NOTE : The path has to end on a leaf node. 

Example :

         1
        /
       2
min depth = 2.
'''
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # post order traversal
    def minDepth(self, root):
        if not root:
            return 0
        # leaf nodes contribute 1 to the depth
        if not root.left and not root.right:
            return 1
        # if there is no left node then add 1 + right subtree
        if root.left is None:
            return 1 + self.minDepth(root.right)
        # if there is no right node then add 1 + left subtree
        if root.right is None:
            return 1 + self.minDepth(root.left)
        return (1 + min(self.minDepth(root.left),self.minDepth(root.right)))
