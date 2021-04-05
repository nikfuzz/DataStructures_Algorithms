'''
Mod Sum

Given an array of integers A, calculate the sum of A [ i ] % A [ j ] for all possible i, j pairs. 
Return sum % (109 + 7) as an output.

Problem Constraints
1 <= length of the array A <= 105
1 <= A[i] <= 103

Input 1:
 A = [1, 2, 3]
Input 2:
 A = [17, 100, 11]

Output 1:
 5
Output 2:
 61
'''

class Solution:
    # calculate frequency of occ
    # group the same occ together and add to answer
    def solve(self, a):
        
        m = 10**9 + 7
        
        max_a = max(a)
        freq = [0 for i in range(max_a+1)]
        
        for i in a:
            freq[i] += 1
        
        ans = 0
        for i in range(1,max_a+1):
            for j in range(1,max_a+1):
                ans += (freq[i] * freq[j]) * (i%j)
                ans = ans % m
        
        return ans