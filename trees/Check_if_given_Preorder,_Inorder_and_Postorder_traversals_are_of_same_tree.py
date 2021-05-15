'''
Check if given Preorder, Inorder and Postorder traversals are of same tree

Given 3 array of integers A, B and C.
A represents preorder traversal of a binary tree.
B represents inorder traversal of a binary tree.
C represents postorder traversal of a binary tree.
Check whether these tree traversals are of the same tree or not. If they are of same tree return 1 else return 0.

Constraints
1 <= length of the array <= 1000
all arrays are of same length
1 <= A[i], B[i], C[i] <= 10^9 
'''
# we will keep making new subarrays based on inorder and preorder traversals, and then check if the same elements exist
# in all the subarrays of the 3 traversals
class Solution:
    def checkOrders(self, pre,inor,post,l):
        if l == 0:
            return 1
        if l == 1:
            return (pre[0]==inor[0] and inor[0]==post[0])
        
        ind = -1
        for i in range(l):
            if inor[i] == pre[0]:
                ind = i
                break
        # if the next root is not found in inorder subarray
        if ind == -1:
            return 0
            
        left = self.checkOrders(pre[1:],inor,post,ind)
        right = self.checkOrders(pre[ind+1:],inor[ind+1:],post[ind:],l-ind-1)
        
        return left and right
    
    def solve(self, a, b, c):
        check = self.checkOrders(a,b,c,len(a))
        if check:
            return 1
        else:
            return 0
# TC O(n)
# SC O(n)