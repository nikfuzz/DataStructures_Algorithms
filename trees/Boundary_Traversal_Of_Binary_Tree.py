'''
Boundary Traversal Of Binary Tree

Given a binary tree. Given a binary tree, return the values of its boundary in anti-clockwise direction starting from the root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.
Left boundary is defined as the path from the root to the left-most node. Right boundary is defined as the path from the root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.
The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.
The right-most node is also defined by the same way with left and right exchanged.
Return an array of integers denoting the boundary values of tree in anti-clockwise order.

Input 1:
               _____1_____
              /           \
             2             3
            / \            / 
           4   5          6   
              / \        / \
             7   8      9  10  
Output 1:
    [1, 2, 4, 7, 8, 9, 10, 6, 3]

Input 2:
                1
               / \
              2   3
             / \  / \
            4   5 6  7
Output 2:
     [1, 2, 4, 5, 6, 7, 3] 
'''
# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None
# To get all the nodes on the left border we do a preorder traversal with small modification to avoid the leaf nodes
# to get the leaf nodes we do an inorder traversal on left and right sub trees
# and finally to get the right boundry in the revserse order we do a post order traversal
class Solution:
    def getRightB(self, root, res):
        if not root: return
        if root.right:
            self.getRightB(root.right, res)
            res.append(root.val)
        elif root.left:
            self.getRightB(root.left, res)
            res.append(root.val)
        return
    
    def getLeaves(self, root, res):
        if not root:
            return
        self.getLeaves(root.left, res)
        if not root.left and not root.right:
            res.append(root.val)
            return
        self.getLeaves(root.right, res)
        return
        
    def getLeftB(self, root, res):
        if not root: return
        if root.left:
            res.append(root.val)
            self.getLeftB(root.left, res)
        elif root.right:
            res.append(root.val)
            self.getLeftB(root.right, res)
        return
    
    def solve(self, root):
        res = []
        res.append(root.val)
        self.getLeftB(root.left, res)
        self.getLeaves(root.left, res)
        self.getLeaves(root.right, res)
        self.getRightB(root.right, res)
        return res
# TC O(n)
# SC O(H) aux space
