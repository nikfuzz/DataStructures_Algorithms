'''
Remove Nth Node from List End

Given a linked list A, remove the B-th node from the end of list and return its head.
For example, Given linked list: 1->2->3->4->5, and B = 2. After removing the second node from the end, the linked list becomes 1->2->3->5.
NOTE: If B is greater than the size of the list, remove the first node of the list.
NOTE: Try doing it using constant additional space.

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 2

Input 2:
A = [1]
B = 1


Example Output
Output 1:
[1, 2, 3, 5]

Output 2:
 [] 
'''
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

# Calculate the length of the list first and subtract b from it so we know which node to remove
# simply traverse to the node and set prev.next to curr.next
class Solution:
    def removeNthFromEnd(self, head, b):
        if head.next == None:
            return None
        len_list = 0
        ptr = head
        while ptr:
            len_list += 1
            ptr = ptr.next
        if b>=len_list:
            head = head.next
            return head
        traverse_count = len_list - b
        ptr = head
        pre = None
        while traverse_count != 0:
            pre = ptr
            ptr = ptr.next
            traverse_count -= 1
        pre.next = ptr.next
        return head
# TC O(n)
# SC O(1), no aux space

