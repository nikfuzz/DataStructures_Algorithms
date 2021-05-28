'''
Merge K Sorted Lists

Given a list containing head pointers of N sorted linked lists. 
Merge these N given sorted linked lists and return it as one sorted list.

Problem Constraints
1 <= total number of elements in given linked lists <= 100000

Example Input
Input 1:

 1 -> 10 -> 20
 4 -> 11 -> 13
 3 -> 8 -> 9
Input 2:

 10 -> 12
 13
 5 -> 6


Example Output
Output 1:

 1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
Output 2:

 5 -> 6 -> 10 -> 12 ->13
'''

import heapq as heap

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Push all the elements from the list in the min heap
# pop the heap, make a node of it, and point ptr.next to the new node
class Solution:
    def mergeKLists(self, a):
        h = []
        for i in range(len(a)):
            start = a[i]
            while start:
                heap.heappush(h, start.val)
                start = start.next
        new_head = ListNode(-1)
        ptr = new_head
        while h:
            ptr.next = ListNode(heap.heappop(h))
            ptr = ptr.next
            if ptr.next:
                heap.heappush(h, ptr.next)
        return new_head.next
# TODO: reduce the time complexity by just having n elements in the heap at a given time
# TC O(m * log m), m is the total number of elements
# SC O(m)