'''
Least Common Ancestor

Find the lowest common ancestor in an unordered binary tree A given two values B and C in the tree.
Lowest common ancestor : the lowest common ancestor (LCA) of two nodes and w in a tree or 
directed acyclic graph (DAG) is the lowest (i.e. deepest) node that has both v and w as descendants.

Problem Constraints
1 <= size of tree <= 100000
1 <= B, C <= 109

Example Input
Input 1:

 
      1
     /  \
    2    3
B = 2
C = 3
Input 2:

      1
     /  \
    2    3
   / \
  4   5
B = 4
C = 5


Example Output
Output 1:

 1
Output 2:

 2
'''

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# first search if both values exist in the tree, if yes
# We traverse left and right subtree and try to find if root is either equal to b or c
# if yes then we return root else we return None when root hits null
# if left and right both are not None then we return root, implying this root has closest access to both vals
# if one of them is set then return that node
class Solution:
    def nodeExists(self, root, key):
        if not root:
            return False
        if root.val == key:
            return True
        left = self.nodeExists(root.left, key)
        if left:
            return True
        
        right = self.nodeExists(root.right, key)
        return right
	
    def lcaUtil(self, root, b, c):
        if not root: return None
        if root.val == b or root.val == c:
            return root
        left = self.lcaUtil(root.left, b, c)
        right = self.lcaUtil(root.right, b, c)
        if left and right:
            return root
        return left or right
	
    def lca(self, root, b, c):
        # check if nodes exist
        if self.nodeExists(root, b) and self.nodeExists(root, c):
            ans = self.lcaUtil(root, b, c)
            return ans.val
        else:
            return -1
# TC O(n)
# SC O(n)
