'''
Min XOR value

Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. 
Report the minimum XOR value.

Problem Constraints:
2 <= length of the array <= 100000
0 <= A[i] <= 109

Input 1:
 A = [0, 2, 5, 7]

Input 2:
 A = [0, 4, 7, 9]

Output 1:
 2
Output 2:
 3
'''

class Solution:
    # min xor can only be obtained between adjacent elements, a[0] ^ a[3] will never be lesser than a[0]^a[1] in a sorted arr
    def findMinXor(self, a):
        a.sort()
        min_x = float('inf')
        for i in range(0,len(a)-1):
            min_x = min(min_x, a[i]^a[i+1])
        return min_x