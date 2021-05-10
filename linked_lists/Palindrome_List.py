'''
Palindrome List

Given a singly linked list A, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Problem Constraints
1 <= |A| <= 105

Example Input
Input 1:

A = [1, 2, 2, 1]
Input 2:

A = [1, 3, 2]


Example Output
Output 1:

 1 
Output 2:

 0 
'''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # reverse the list from mid
    # compare list from the two ends
    # stop when p1 == p2 or until p1 and p2 exists
    def lPalin(self, head):
        if not head.next:
            return 1
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            # to keep curr on the last node
            if not next:
                break
            curr = next
        p2 = curr
        p1 = head
        while p1!=p2 and (p1 and p2):
        	if p1.val != p2.val:
        		return 0
        	p1 = p1.next
        	p2 = p2.next
        return 1
#  TC O(n)
#  SC O(1)

