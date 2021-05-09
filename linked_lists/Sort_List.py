'''
Sort List

Sort a linked list, A in O(n log n) time using constant space complexity.

Problem Constraints
0 <= |A| = 105

Example Input
Input 1:

A = [3, 4, 2, 8]
Input 2:

A = [1]


Example Output
Output 1:

[2, 3, 4, 8]
Output 2:

[1]
'''

import sys
sys.setrecursionlimit(10**6)
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# use merge sort on the list
# find mid using slow and fast pointer
# for merging compare values of the nodes on left and right
class Solution:
    def sortList(self, head):
        if not head or not head.next: return head
        mid = self.findMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeList(left,right)
    
    def mergeList(self,left,right):
        dummy = curr = ListNode(0)
        while left and right:
        	if left.val < right.val:
        		curr.next = left
        		curr = curr.next
        		left = left.next
        	else:
        		curr.next = right
        		curr = curr.next
        		right = right.next
        # remaining nodes from left or right
        curr.next = left or right
        return dummy.next

    def findMid(self, head):
    	fast, slow = head, head
    	while fast.next and fast.next.next:
    		fast = fast.next.next
    		slow = slow.next
    	mid = slow.next
        # next of mid should be null, to hit the base condition in out recurring function
    	slow.next = None
    	return mid
# TC O(n log(n))
# SC O(n) but O(1) extra aux space



