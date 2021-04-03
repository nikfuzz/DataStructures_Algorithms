'''
Interesting Array

You have an array A with N elements. We have 2 types of operation available on this array :
We can split a element B into 2 elements C and D such that B = C + D.
We can merge 2 elements P and Q as one element R such that R = P^Q i.e XOR of P and Q.
You have to determine whether it is possible to make array A containing only 1 element i.e. 0 after several splits and/or merge?

Problem Constraints
1 <= N <= 100000
1 <= A[i] <= 106

Input 1:
 A = [9, 17]

Input 2:
 A = [1]

Output 1:
 Yes

Output 2:
 No
'''

class Solution:
    # all even numbers become 0 when split then merged
    # all odd nos give even + 1 on split
    # so if we have even nos of 1 then we can merge them to form an even integer which can further be reduced to 0
    def solve(self, a):
        count_odd = 0
        for i in range(len(a)):
            if a[i] & 1 == 1:
                count_odd += 1
        
        if count_odd & 1 == 0:
            return "Yes"
        return "No"
