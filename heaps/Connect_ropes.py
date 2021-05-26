'''
Connect ropes

Given an array of integers A representing the length of ropes.
You need to connect these ropes into one rope. The cost of connecting two ropes is equal to the sum of their lengths.
Find and return the minimum cost to connect these ropes into one rope.

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 1000

Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [5, 17, 100, 11]


Example Output
Output 1:

 33
Output 2:

 182
'''

# min heapify arr
# pop the first two ropes from the heap and take their sum
# add their sum to the cost and push the sum to the heap
# do this until length of heap becomes 1, i.e, all the ropes are connected
import heapq
class Solution:
    def solve(self, a):
        cost = 0
        heapq.heapify(a)
        while len(a) > 1:
            rope1 = heapq.heappop(a)
            rope2 = heapq.heappop(a)
            cost += rope1 + rope2
            heapq.heappush(a, rope1 + rope2)
        return cost
# TC O(n*log n)
# SC O(n)
