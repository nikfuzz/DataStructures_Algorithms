'''
Swap List Nodes in pairs

Given a linked list A, swap every two adjacent nodes and return its head.
NOTE: Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

Example Input
Input 1:

 A = 1 -> 2 -> 3 -> 4
Input 2:

 A = 7 -> 2 -> 1


Example Output
Output 1:

 2 -> 1 -> 4 -> 3
Output 2:

 2 -> 7 -> 1
'''

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# make a dummy node which points to the head
# start curr from the dummy node
# swap curr.next and curr.next.next
# move curr to curr.next.next
# return dummy.next 

class Solution:
    def swapFunc(self, next1, next2):
    	next1.next = next2.next
    	next2.next = next1
    	return next2
    
    def swapPairs(self, head):
    	if head.next == None:
    		return head
    	start = ListNode(0)
    	start.next = head
    	curr = start
    	while curr.next and curr.next.next:
    		curr.next = self.swapFunc(curr.next,curr.next.next)
    		curr = curr.next.next
    	return start.next

# TC O(n)
# SC O(1)
