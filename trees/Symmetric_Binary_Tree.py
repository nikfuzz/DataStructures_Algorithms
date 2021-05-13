'''
Symmetric Binary Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Problem Constraints
1 <= number of nodes <= 105

Example Input
Input 1:

    1
   / \
  2   2
 / \ / \
3  4 4  3
Input 2:

    1
   / \
  2   2
   \   \
   3    3


Example Output
Output 1:

 1
Output 2:

 0
'''

from collections import deque

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None 

# since we need to check for a mirror image we can say that the pre-order or left sub tree == post-order right sub tree
# add preorder elements from left subtree in a stack
# do a post order traversal on right sub tree and return False if the stack is empty or stack[-1] != root.val
class Solution:
    def preorder(self, root, left_pre):
        if not root:
            return 
        left_pre.append(root.val)
        self.preorder(root.left, left_pre)
        self.preorder(root.right,left_pre)
	
    def postorder(self, root, check):
        if not root:
            return
        self.postorder(root.left, check)
        self.postorder(root.right, check)
        if not check or (root and root.val != check.pop()):
            return False

    def isSymmetric(self, root):
        left_pre = deque()
        self.preorder(root.left, left_pre)
        # To do: This condition could be handled better
        if self.postorder(root.right,left_pre) == False:
            return 0
        else:
            return 1
# TC O(n)
# SC O(n)