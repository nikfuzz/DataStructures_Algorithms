'''
Product of 3

Given an integer array A of size N.
You have to find the product of the 3 largest integers in array A from range 1 to i, where i goes from 1 to N.
Return an array B where B[i] is the product of the largest 3 integers in range 1 to i in array A. If i < 3, then the integer at index i is -1.

Problem Constraints
1 <= N <= 105
0 <= A[i] <= 103

Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [10, 2, 13, 4]


Example Output
Output 1:

 [-1, -1, 6, 24, 60]
Output 2:

 [-1, -1, 260, 520]
'''

import heapq

# add first 3 elements in heap and append -1 twice and product of th first 3 elements in the result
# start the loop from 3rd pos
# if the new incoming number is greater than the min element in the heap then we remove the top of heap and add a[i]
# append the new product in res
# if the new element is not greater than heap[0] then our curr result will be same as last one
class Solution:
    def solve(self, a):
        # if length is less than 3 then we just return an arr of -1s
        if len(a) < 3:
            return [-1]*len(a)
        heap = []
        res = []
        pro = a[0]*a[1]*a[2]
        heapq.heappush(heap,a[0])
        res.append(-1)
        heapq.heappush(heap,a[1])
        res.append(-1)
        heapq.heappush(heap,a[2])
        res.append(pro)
        for i in range(3,len(a)):
            if a[i] > heap[0] and len(heap)>=3:
                pro = res[-1]//heap[0]
                heapq.heappushpop(heap,a[i])
                pro *= a[i]
                res.append(pro)
            else:
                res.append(res[-1])
        return res
# TC O(n log n)
# SC O(1), since at any given point we will have only 3 elements in the heap
