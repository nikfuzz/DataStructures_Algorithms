'''
Maximum array sum after B negations

Given an array of integers A and an integer B. You must modify the array exactly B number of times. 
In single modification, we can replace any one array element A[i] by -A[i].
You need to perform these modifications in such a way that after exactly B modifications, sum of the array must be maximum.

Problem Constraints
1 <= length of the array <= 5*10^5
1 <= B <= 5 * 10^6
-100 <= A[i] <= 100

Example Input
Input 1:

 A = [24, -68, -29, -9, 84]
 B = 4
Input 2:

 A = [57, 3, -14, -87, 42, 38, 31, -7, -28, -61]
 B = 10


Example Output
Output 1:

 196
Output 2:

 362
'''
# min heapify arr
# pop the min element in the heap and multiple it by -1
# we need to make exactly b modifications so if we end up switching the same element again and again, it is a necessary operation
# finally return the sum of the heap
import heapq as heap
class Solution:
    def solve(self, a, b):
        heap.heapify(a)
        for i in range(b):
            num = heap.heappop(a)
            num = -1 * num
            heap.heappush(a, num)
        return sum(a)
# TC O(n * log n)
# SC O(n)