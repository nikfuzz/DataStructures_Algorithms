'''
Magician and Chocolates

Given N bags, each bag contains Bi chocolates. There is a kid and a magician. In one unit of time, kid chooses a random bag i, eats Bi chocolates, then the magician fills the ith bag with floor(Bi/2) chocolates.
Find the maximum number of chocolates that kid can eat in A units of time.
NOTE:
floor() function returns the largest integer less than or equal to a given number.
Return your answer modulo 109+7

Problem Constraints
1 <= N <= 100000
0 <= B[i] <= INT_MAX
0 <= A <= 105

Example Input
Input 1:

 A = 3
 B = [6, 5]
Input 2:

 A = 5
 b = [2, 4, 6, 8, 10]


Example Output
Output 1:

 14
Output 2:

 33
'''
# create a max heap
# add max val from heap to the final ans and pop it
# add max_val//2 in the heap
# do above 2 steps 'a' times
import heapq
class Solution:
    def nchoc(self, a, b):
        heap = []
        for i in range(len(b)):
            heapq.heappush(heap,-1 * b[i])
        tc = 0
        for i in range(a):
            max_val = -1 * heapq.heappop(heap)
            tc += (max_val)
            heapq.heappush(heap, -1*(max_val//2))
        return tc % (10**9 + 7)
# TC O(n) + O(a*log n), n in the no of elements in b
# SC O(n)