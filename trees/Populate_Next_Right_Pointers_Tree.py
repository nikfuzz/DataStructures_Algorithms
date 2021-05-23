'''
Populate Next Right Pointers Tree

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 Note:
You may only use constant extra space.
Example :

Given the following binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
'''
# we connect the left child of root to the right child.
# if there is no right child we move to the next horizontal node that is available and connect its first child
class Solution:
    # func to return the next available node
    def getNextRight(self, q):
        q = q.next
        while q:
            if q.left: 
                return q.left
            if q.right: 
                return q.right
            q = q.next
        return q
    
    def connect(self, root):
        p = root
        while p:
            q = p
            while q:
                if q.left:
                    if q.right:
                        q.left.next = q.right
                    else:
                        q.left.next = self.getNextRight(q)
                if q.right:
                    q.right.next = self.getNextRight(q)
                q = q.next
            if p.left:
                p = p.left
            elif p.right:
                p = p.right
            else:
                p = self.getNextRight(p)
        return root
# TC O(n)
# SC O(1)