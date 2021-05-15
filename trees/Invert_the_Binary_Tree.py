'''
Invert the Binary Tree

Given a binary tree A, invert the binary tree and return it.
Inverting refers to making left child as the right child and vice versa.

Problem Constraints
1 <= size of tree <= 100000

Example Input
Input 1:

 
     1
   /   \
  2     3
Input 2:

 
     1
   /   \
  2     3
 / \   / \
4   5 6   7


Example Output
Output 1:

 
     1
   /   \
  3     2
Output 2:

 
     1
   /   \
  3     2
 / \   / \
7   6 5   4
'''

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# just swap left and right node
# and follow the pre order traversal
class Solution:
    def invertTree(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
# TC O(n)
# SC O(n)
