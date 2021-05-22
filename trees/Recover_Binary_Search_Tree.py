'''
Recover Binary Search Tree

Two elements of a binary search tree (BST),represented by root A are swapped by mistake. Tell us the 2 values swapping which the tree will be restored.
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

Problem Constraints
1 <= size of tree <= 100000

'''

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
# We will keep a prev pointer, n1- first element to swap, n2- second element to swap
# We will pass these pointers as arrays because we need to call by reference, arrays are mutable
# prev will point to the prev root node in inorder arrangement
# if prev > root then we set n1 to prev and n2 to root, this is the case where we assume prev and root are the elements to swap
# But if we find another abnormality then we have to sort the old node which was set in n1 and the curr node which will be set to n2
class Solution:
    def recoverTreeUtil(self,root,n1,n2,prev):
        if not root:
            return
        self.recoverTreeUtil(root.left,n1,n2,prev)
        if prev[0]:
            if prev[0].val > root.val:
                if not n1[0]:
                    n1[0] = prev[0]
                    n2[0] = root
                else:
                    n2[0] = root
        prev[0] = root
        self.recoverTreeUtil(root.right,n1,n2,prev)
        return
        
        
    def recoverTree(self, root):
        n1, n2 = [None], [None]
        prev = [None]
        self.recoverTreeUtil(root,n1,n2,prev)
        return [n2[0].val,n1[0].val]
# TC O(n)
# SC O(H), height of the bst