'''
Ath largest element

Given an integer array B of size N.
You need to find the Ath largest element in the subarray [1 to i] where i varies from 1 to N. In other words, find the Ath largest element in the sub-arrays [1 : 1], [1 : 2], [1 : 3], ...., [1 : N].
NOTE: If any subarray [1 : i] has less than A elements then output array should be -1 at the ith index.

Problem Constraints
1 <= N <= 100000
1 <= A <= N
1 <= B[i] <= INT_MAX

Example Input
Input 1:

 A = 4  
 B = [1 2 3 4 5 6] 
Input 2:

 A = 2
 B = [15, 20, 99, 1]


Example Output
Output 1:

 [-1, -1, -1, 1, 2, 3]
Output 2:

 [-1, 15, 20, 20]
'''
# first insert a elements in a min heap.
# if i < a: append -1 in the result array
# if i == a append heap[0] in res
# now check for remaining elements in len(b)
# if top of heap < b[i] then pop the top element and push b[i], and then append the new top in the res
# else just append heap top in the res
import heapq as heap
class Solution:
    def solve(self, a, b):
        h = []
        res = []
        for i in range(a):
            heap.heappush(h,b[i])
            if i<a-1:
                res.append(-1)
            else:
                res.append(h[0])
        for i in range(a,len(b)):
            if h[0]<b[i]:
                heap.heappop(h)
                heap.heappush(h, b[i])
            res.append(h[0])
        return res
# TC O(n * log a)
# SC O(a)
            
            
