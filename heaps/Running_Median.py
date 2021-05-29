'''
Running Median

Given an array of integers A denoting a stream of integers. New arrays of integer B and C are formed. 
Each time an integer is encountered in a stream, append it at the end of B and append median of array B at the C.
Find and return the array C.
NOTE:
If the number of elements are N in B and N is odd then consider medain as B[N/2] ( B must be in sorted order).
If the number of elements are N in B and N is even then consider medain as B[N/2-1]. ( B must be in sorted order).

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109

Example Input
Input 1:

 A = [1, 2, 5, 4, 3]
Input 2:

 A = [5, 17, 100, 11]


Example Output
Output 1:

 [1, 1, 2, 2, 3]
Output 2:

 [5, 5, 17, 11]
'''
# maintain a min and a max heap
# when an element is added from the stream we check if the number is greater than the max heap's top
# if it is greater then we add it to the min heap else we add it to the max heap
# for appending the result:
# if len of the 2 heaps is same then we take the top of max heap (left side of the arr)
# if the diff between lengths is 1 then we take the root of the bigger heap
# if the diff > 1 then we pop the top of the larger heap and add it to the smaller heap and append the top of the max heap to res
import heapq
class Solution:
    def solve(self, a):
        mi = []
        ma = []
        res = []
        for i in range(len(a)):
            if not mi and not ma:
                heapq.heappush(ma, -1 * a[i])
            elif a[i] > (-1 * ma[0]):
                heapq.heappush(mi, a[i])
            else:
                heapq.heappush(ma, -1 * a[i])
            if len(ma) == len(mi):
                res.append(-1 * ma[0])
            elif abs(len(mi)-len(ma)) == 1:
                if len(mi) > len(ma):
                    res.append(mi[0])
                else:
                    res.append(-1*ma[0])
            else:
                if len(mi) > len(ma):
                    heapq.heappush(ma, -1 * mi[0])
                    heapq.heappop(mi)
                else:
                    heapq.heappush(mi, -1 * ma[0])
                    heapq.heappop(ma)
                res.append(-1 * ma[0])
        return res
# TC O(n * log n)
# SC O(n)