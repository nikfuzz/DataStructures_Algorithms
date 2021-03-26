'''
First Missing Integer

Given an unsorted integer array A of size N. Find the first missing positive integer.
Note: Your algorithm should run in O(n) time and use constant space.

Constraints:
1 <= N <= 1000000
-109 <= A[i] <= 109

input: [1, 2, 0]
output: 3

input: [-8, -7, -6]
output: 1
'''

def firstMissingPositive(a):
    i = 0
    n = len(a)
    
    # check if 1 is missing
    if 1 not in a:
        return 1
    
    # make all neg nos and >N nos = 1
    for i in range(n):
        if a[i] <= 0 or a[i] > n:
            a[i] = 1
    
    # add n to the a[i] indexes
    for i in range(n):
        a[(a[i]-1)%n] += n
    
    # the missing number will give a val less than n when indexed
    for i in range(n):
        if a[i] <= n:
            return (i+1)
        
    return n+1