'''
Rain Water Trapped

Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.


constraints:
1 <= |a| <= 100000

a is the array of integers

input: [ 3, 0, 2, 0, 4 ]
output: 7

input: [ 0, 1, 0, 2 ]
output: 1
'''

def trap(a):
    n = len(a)
    pre = [None]*n
    suff = [None]*n
    pre[0] = 0
    suff[n-1] = 0
    for i in range(1,n):
        pre[i] = max(a[i-1], pre[i-1])
    for j in range(n-2, -1, -1):
        suff[j] = max(suff[j+1], a[j+1])
    sum = 0
    for i in range(0,n):
        h = min(pre[i],suff[i]) - a[i]
        if h > 0:
            sum += h
    return sum