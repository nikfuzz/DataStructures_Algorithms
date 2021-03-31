'''
A, B and Modulo

Given two integers A and B, find the greatest possible positive M, such that A % M = B % M.

constraints:
1 <= A, B <= 109
A != B

input: A=1, B=2
output: 1

input: A=5, B=10
output: 5
'''
class Solution:
    # the diff of the two nos gives the same reminder when it divides the nos.
    def solve(self, a, b):
        return abs(a-b)