'''
Different Bits Sum Pairwise

We define f(X, Y) as number of different corresponding bits in binary representation of X and Y.
For example, f(2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f(2, 7) = 2.

You are given an array of N positive integers, A1, A2 ,..., AN. Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.

Problem Constraints:
1 <= N <= 105
1 <= A[i] <= 231 - 1

Input 1:
 A = [1, 3, 5]
Input 2:
 A = [2, 3]

Ouptut 1:
 8
Output 2:
 2
'''

class Solution:
	def cntBits(self, a):
	    sum = 0
	    m = 10**9 + 7
	    # count the number of 1s in each parity of every number
	    for i in range(32):
	        count_1 = 0
	        for j in range(len(a)):
	            if a[j] & (1<<i):
	                count_1 += 1
            # multiply number of 1s with number of 0s, this will give us number of diff bits for all pairs in that parity
            # multiple by 2 because we can have f(i,i) too
	        sum += 2 * count_1 * (len(a)-count_1)
	        sum = sum % m
	    return sum