'''
Sum of all Submatrices

Given a 2D Matrix A of dimensions N*N, we need to return sum of all possible submatrices.

Constraints:
1 <= N <=30
0 <= A[i][j] <= 10

input: [ [1, 1]
      [1, 1] ]

output: 16
'''

def solve(a):
    sum = 0
    # We need to find the contribution of each element in all the subarrays towards the total sum
    for i in range(len(a)):
        for j in range(len(a[i])):
            count_tc = (i+1)*(j+1)
            count_bc = (len(a)-i)*(len(a[i])-j)
            
            sum += a[i][j] * (count_tc * count_bc)
    return sum