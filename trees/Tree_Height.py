'''
Tree Height

You are given the root node of a binary tree A, You have to find the height of the given tree.
A binary tree's height is the number of nodes along the longest path from the root node down to the farthest leaf node.

Problem Constraints
1 <= Number of nodes in the tree <= 105
0 <= Value of each node <= 109

Example Input
Input 1:

 Values =  1 
          / \     
         4   3                        
Input 2:

 
 Values =  1      
          / \     
         4   3                       
        /         
       2                                     


Example Output
Output 1:

 2 
Output 2:

 3 
'''
# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# Keep adding 1 at each recursive depth
# final answer should return 1 + max(left subtree, right sub tree)
class Solution:
    def solve(self, root):
        if not root: 
            return 0
        left = self.solve(root.left)
        right = self.solve(root.right)
        return 1+max(left,right)
# TC O(n)
# SC O(n)
