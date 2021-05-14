'''
Binary Tree From Inorder And Preorder

Given preorder and inorder traversal of a tree, construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.

Problem Constraints
1 <= number of nodes <= 105

Example Input
Input 1:

 A = [1, 2, 3]
 B = [2, 1, 3]
Input 2:

 A = [1, 6, 2, 3]
 B = [6, 1, 3, 2]


Example Output
Output 1:

   1
  / \
 2   3
Output 2:

   1  
  / \
 6   2
    /
   3
'''

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# first element of pre will give the root
# all the elements to the right of the root in inorder will be left subtree and elements on the right will give right sub tree
# set range of pre order from start to start + number of elements for LEFT SUB TREE
# set range of pre order from start + number of elements + 1 to end for RIGHT SUB TREE
class Solution:
    map = {}
    def createTree(self,inor,s1,e1,pre,s2,e2):
        # end of range
        if s1 > e1 or s2 > e2:
            return 
        root = TreeNode(pre[s2])
        # end of the branch
        if not root:
            return
        pos = self.map[pre[s2]]
        noe = pos - s1
        root.left = self.createTree(inor, s1, pos-1, pre, s2+1, s2+noe)
        root.right = self.createTree(inor, pos+1, e1, pre, s2+noe+1, e2)
        
        return root
	
    def buildTree(self, pre, inor):
        self.map = {}
        for i in range(len(inor)):
            self.map[inor[i]] = i
            
        return self.createTree(inor, 0, len(inor)-1, pre, 0, len(pre)-1)
# TC O(n)
# SC O(n)
