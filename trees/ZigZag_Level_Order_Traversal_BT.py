'''
ZigZag Level Order Traversal BT

Given a binary tree, return the zigzag level order traversal of its nodes values. (ie, from left to right, then right to left for the next level and alternate between).

Problem Constraints
1 <= number of nodes <= 105

Example Input
Input 1:

    3
   / \
  9  20
    /  \
   15   7
Input 2:

   1
  / \
 6   2
    /
   3


Example Output
Output 1:

 [
   [3],
   [20, 9],
   [15, 7]
 ]
Output 2:

 [ 
   [1]
   [2, 6]
   [3]
 ]
'''

from collections import deque
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # make an odd stack for odd levels and even stack for even levels
    # each of these stacks will hold all the nodes for a level
    # when going through odd stack append left child and right child(in that order) of the odd's top node, in the even stack
    # and when going through even stack append right and left child(in that order) of the even's top node, in the odd stack
    # append the list after popping all the elements of one stack
    def zigzagLevelOrder(self, root):
        os = deque()
        es = deque()
        res = []
        os.append(root)
        while os or es:
            lvl = []
            while os:
                node = os.pop()
                if node.left:
                    es.append(node.left)
                if node.right:
                    es.append(node.right)
                lvl.append(node.val)
            if lvl:
                res.append(lvl)
                lvl = []
            while es:
                node = es.pop()
                if node.right:
                    os.append(node.right)
                if node.left:
                    os.append(node.left)
                lvl.append(node.val)
            if lvl:
                res.append(lvl)
        return res
# TC O(n)
# SC O(n)
        
        
        
