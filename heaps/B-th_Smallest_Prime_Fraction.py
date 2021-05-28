'''
B-th Smallest Prime Fraction

A sorted array of integers, A contains 1, plus some number of primes. Then, for every p < q in the list, we consider the fraction p/q.
What is the B-th smallest fraction considered?
Return your answer as an array of integers, where answer[0] = p and answer[1] = q.

Problem Constraints
1 <= length(A) <= 2000
1 <= A[i] <= 30000
1 <= B <= length(A)*(length(A) - 1)/2

Example Input
Input 1:

 A = [1, 2, 3, 5]
 B = 3
Input 2:

 A = [1, 7]
 B = 1


Example Output
Output 1:

 [2, 5]
Output 2:

 [1, 7]
'''
# for every i move j from right to i + 1 and,
# add all the elements in a min heap => (a[i]/a[j], a[i], a[j])
# pop b-1 elements and return root's a[i] and a[j] part
import heapq
class Solution:
    def solve(self, a, b):
        i = 0
        j = len(a)-1
        heap = []
        while i < len(a)-1:
            j = len(a)-1
            while j > i:
                heap.append((a[i]/a[j], a[i], a[j]))
                j -= 1
            i += 1
        heapq.heapify(heap)
        for i in range(b-1):
            heapq.heappop(heap)
        return [heap[0][1], heap[0][2]]
# TC O(n * log n)
# SC O(n)