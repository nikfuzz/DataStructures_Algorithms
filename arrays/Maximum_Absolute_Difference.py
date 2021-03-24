'''
Maximum Absolute Difference
You are given an array of N integers, A1, A2, .... AN.
Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

Constraints:
1 <= N <= 100000
-109 <= A[i] <= 109

input: [1, 3, -1]
output: 5

input: [2]
output: 0
'''

def maxArr(self, a):
    # absolute sol can be broken down to 2 diff equations based on its defination
    # rearranging them will give a[i]+i - a[j] + j and a[i]-i - a[j]-j
    # since there is no relation between and i and j we can say i == j is possible
    ma1 = float('-inf')
    mi1 = float('inf')
    ma2 = ma1
    mi2 = mi1
    
    # we need the max of the operation that is contributing to the sum and min of the operation that is being deducted
    for i in range(len(a)):
        ma1 = max(ma1,a[i]+i)
        mi1 = min(mi1,a[i]+i)
        ma2 = max(ma2,a[i]-i)
        mi2 = min(mi2,a[i]-i)
        
    return max((ma1-mi1),(ma2-mi2))

