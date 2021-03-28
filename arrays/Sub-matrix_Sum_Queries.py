'''
Sub-matrix Sum Queries

Given a matrix of integers A of size N x M and multiple queries Q, for each query find and return the submatrix sum.
Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.
NOTE:
Rows are numbered from top to bottom and columns are numbered from left to right.
Sum may be large so return the answer mod 109 + 7.

Constraints:
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
1 <= Q <= 100000
1 <= B[i] <= D[i] <= N
1 <= C[i] <= E[i] <= M

input:  
A = [   [1, 2, 3]
         [4, 5, 6]
         [7, 8, 9]   ]
 B = [1, 2]
 C = [1, 2]
 D = [2, 3]
 E = [2, 3]

 output: [12, 28]

input:
 A = [   [5, 17, 100, 11]
         [0, 0,  2,   8]    ]
 B = [1, 1]
 C = [1, 4]
 D = [2, 2]
 E = [2, 4]

output: [22, 19]
'''

def solve(a, b, c, d, e):
    n = len(a)
    m = len(a[0])
    pref = a
    res = []

    # create a row plus col prefix arr
    for i in range(0,n):
        pref[i][0] = a[i][0]
        for j in range(1,m):
            pref[i][j] = (pref[i][j-1] % (10**9 + 7) + a[i][j] % (10**9 + 7)) % (10**9 + 7)
    
    for i in range(0,m):
        for j in range(1,n):
            pref[j][i] = (pref[j-1][i] % (10**9 + 7) + pref[j][i] % (10**9 + 7)) % (10**9 + 7)
        
    # subtract the left and top of the desired matrix, in doing so we remove the common corner element twice so add that
    # ans = pref[bi][bj] - pref[bi][tj-1] - pref[ti-1][bj] + pref[ti-1][tj-1]
    # if the matrix is on topmost or leftmost section then dont subtract the part which has index 0
    for i in range(len(b)):
        ti = b[i] - 1
        tj = c[i] - 1
        bi = d[i] - 1
        bj = e[i] - 1
        ans = pref[bi][bj] 
        
        if tj > 0:
            ans -= pref[bi][tj-1] % (10**9 + 7)
        
        if ti > 0:
            ans -= pref[ti-1][bj] % (10**9 + 7) 
        
        if ti > 0 and tj > 0:
            ans += pref[ti-1][tj-1] % (10**9 + 7)
            
        res.append(ans % (10**9 + 7))
    return res