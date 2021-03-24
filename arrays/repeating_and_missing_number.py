'''
Repeating and missing number in an array

You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.

input: [3 1 2 5 3] 
output: [3, 4] 

'''


import numpy as np

def repeatedNumber(a):
    # We need two equations to find missing num (m) and repeating num (r)
    # calculate sum of n ints
    n = len(a)
    sn = (n*(n+1)) // 2
    # sum of all elements in arr
    sa = sum(a)

    # calculate sq of n natural nums and sq of arr elements
    ssa = sum([x*x for x in a])
    ssn = (n*(n+1)*(2*n+1))//6

    # eq1: m-r = sn-sa eq2: m+r = (ssn-ssa)/(sn-sa)
    
    A = np.array([[1, -1],[1, 1]])
    B = np.array([sn-sa,(ssn-ssa)/(sn-sa)])
    z = np.linalg.solve(A,B)
    return[int(z[1]),int(z[0])]