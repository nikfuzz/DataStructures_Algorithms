'''
K Places Apart

Given N persons with different priorities standing in a queue.
Queue is following a property that Each person is standing atmost B places away from it's sorted position.
Your task is to sort the queue in the increasing order of priorities.
NOTE:
No two persons can have the same priority.
Use the property of the queue to sort the queue with complexity O(NlogB).

Problem Constraints
1 <= N <= 100000
0 <= B <= N

Example Input
Input 1:

 A = [1, 40, 2, 3]
 B = 2
Input 2:

 A = [2, 1, 17, 10, 21, 95]
 B = 1


Example Output
Output 1:

 [1, 2, 3, 40]
Output 2:

 [1, 2, 10, 17, 21, 95]
'''
# add b elements in a min heap
# if i+b < len(a) add i+bth element in the heap
# put heap.pop in place of a[i], this will return the shortest element for that pos
# once we keep putting shortest element for k+1 values we will get a sorted array
import heapq as heap

class Solution:
    def solve(self, a, b):
        h = []
        for i in range(b):
            heap.heappush(h, a[i])
        for i in range(len(a)):
            if i+b < len(a):
                heap.heappush(h, a[i+b])
            a[i] = heap.heappop(h)
        return a
# TC O(n * log b)
# SC O(b)