'''
Reorder List

Given a singly linked list A
 A: A0 → A1 → … → An-1 → An 
reorder it to:
 A0 → An → A1 → An-1 → A2 → An-2 → … 
You must do this in-place without altering the nodes' values.

Problem Constraints
1 <= |A| <= 106

Example Input
Input 1:

 A = [1, 2, 3, 4, 5] 
Input 2:

 A = [1, 2, 3, 4] 


Example Output
Output 1:
 [1, 5, 2, 4, 3] 

Output 2:
 [1, 4, 2, 3] 
'''
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None


# reverse the list from middle
# move the pointer from both sides and change the pointers to point at alternative nodes
class Solution:
    def reorderList(self, head):
        if (not head) or (not head.next):
            return head

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        curr = slow
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            if not next:
                break
            curr = next
        head2 = curr
        ptr1 = head
        ptr2 = head2
        temp = head
        while ptr1.next and ptr2.next:
            ptr1 = ptr1.next
            temp.next = ptr2
            temp = ptr2
            ptr2 = ptr2.next
            temp.next = ptr1
            temp = ptr1
        return head
# TC O(n)
# SC O(1)
        
        
