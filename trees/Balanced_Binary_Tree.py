'''
Balanced Binary Tree

Given a root of binary tree A, determine if it is height-balanced.
A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Problem Constraints
1 <= size of tree <= 100000

Example Input
Input 1:

    1
   / \
  2   3
Input 2:

 
       1
      /
     2
    /
   3


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

# class to store the height of the node and whether it is balanced or not 
class Info:
    def __init__(self,h,isB):
        self.h = h
        self.isB = isB
# In order for the tree to be balanced, all the sub trees must be balanced
# we need to send isBalanced and height for every node
# we send max(height) + 1 and isB == 1 if abs(l.h-r.h)<=1
class Solution:
    def isBalancedUtil(self, root):
        if not root: return Info(0,1)
        l = self.isBalancedUtil(root.left)
        if l.isB != 1:
            return(Info(1, 0))
        r = self.isBalancedUtil(root.right)
        
        if l.isB == 1 and r.isB == 1 and abs(l.h-r.h)<=1:
            return(Info(1+max(l.h,r.h), 1))
        else:
            return(Info(1+max(l.h,r.h), 0))
    def isBalanced(self, root):
        return self.isBalancedUtil(root).isB
# TC O(n)
# SC O(n)
	    