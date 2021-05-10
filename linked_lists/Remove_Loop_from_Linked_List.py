'''
Remove Loop from Linked List

Given a linked list which contains some loop.
You need to find the node, which creates a loop, and break it by making the node point to NULL.

Problem Constraints
1 <= number of nodes <= 1000

Example Input
Input 1:

 
1 -> 2
^    |
| - - 
Input 2:

3 -> 2 -> 4 -> 5 -> 6
          ^         |
          |         |    
          - - - - - -


Example Output
Output 1:

 1 -> 2 -> NULL
Output 2:

 3 -> 2 -> 4 -> 5 -> 6 -> NULL
'''
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

# set a fast pointer of 2x speed and a slow pointer of x speed
# since mathematically the distance between a 2x and x pointer reduces by 1, 
# we can say that they will definitely meet at a point in a loop
# suppose they meet at d + k distance, d is head to loop-start and k is some dist in the loop
# then d+k = n x l, which means we just need to find d distance from k to reach at the beginning of the loop
# that can be found by starting a pointer from k and one from start and check where they meet
class Solution:
    def solve(self, head):
        if not head.next:
        	return head
        slow = fast = head
        slow = slow.next
        fast = slow.next
        while fast != slow:
        	slow  = slow.next
        	fast = fast.next.next
        p1 = slow
        p2 = head
        while p1.next != p2.next:
        	p1 = p1.next
        	p2 = p2.next
        p1.next = None
        return head
# TC O(n)
# SC O(1)

