'''
Reverse Link List II

Reverse a linked list A from position B to C.
NOTE: Do it in-place and in one-pass.

Problem Constraints
1 <= |A| <= 106
1 <= B <= C <= |A|

Example Input
Input 1:

 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 2
 C = 4

Input 2:

 A = 1 -> 2 -> 3 -> 4 -> 5
 B = 1
 C = 5


Example Output
Output 1:

 1 -> 4 -> 3 -> 2 -> 5
Output 2:

 5 -> 4 -> 3 -> 2 -> 1
'''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

# set prev to node before b and curr to b node
# reverse the list till c nodes
# the initial curr before rev should point to the new curr after rev, same with prev
class Solution:
    def reverseBetween(self, head, b, c):
        if not head or not head.next:
            return head
        curr = head
        prev = None
        while b>1:
            prev = curr
            curr = curr.next
            b -= 1
            c -= 1
        before_rev = prev
        tail = curr
        
        while c:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            c -= 1
        # checking if the whole list was reversed
        if before_rev:
            before_rev.next = prev
        else:
            head = prev
        tail.next = curr
            
        return head
# TC O(n)
# SC O(1)


