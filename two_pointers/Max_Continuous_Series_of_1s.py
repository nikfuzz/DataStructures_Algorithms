'''
Max Continuous Series of 1s

Given a binary array A, find the maximum sequence of continuous 1's that can be formed by replacing at-most B zeroes.
For this problem, return the indices of maximum continuous series of 1s in order.
If there are multiple possible solutions, return the sequence which has the minimum start index.

Problem Constraints
0 <= B <= 105
1 <= size(A) <= 105
A[i]==0 or A[i]==1

Example Input
Input 1:
 A = [1 1 0 1 1 0 0 1 1 1 ]
 B = 1

Input 2:
 A = [1, 0, 0, 0, 1, 0, 1]
 B = 2


Example Output
Output 1:
 [0, 1, 2, 3, 4]

Output 2:
 [3, 4, 5, 6]
'''
class Solution:
    def maxone(self, a, b):
        res = []
        c_0 = 0
        c_1 = 0

        i = l = 0
        j = r = 0
        ans = 0

        # count the number of 1s and 0s until the count of 0s <= b
        # if the count exceeds we start removing elements by inc i until the 0s <= b

        while j < len(a) and i<len(a):
            if c_0<=b:
                if a[j] == 0:
                    c_0 += 1
                elif a[j] == 1:
                    c_1 += 1
                if (j-i)>ans and c_0<=b:
                    l = i
                    r = j
                    ans = j-i
                j += 1
            else:
                if a[i] == 1:
                    c_1 -= 1
                else:
                    c_0 -= 1
                i += 1
        res = [x for x in range(l,r+1)]
        return res