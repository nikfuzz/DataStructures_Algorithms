'''
Damaged Roads

You are the Prime Minister of a country and once you went for a world tour.
After 5 years, when you returned to your country, you were shocked to see the condition of the roads between the cities. So, you plan to repair them, but you cannot afford to spend a lot of money.
The country can be represented as a (N+1) x (M+1) grid, where Country(i, j) is a city.
The cost of repairing a road between (i, j) and (i + 1, j) is A[i]. The cost of repairing a road between (i, j) and (i, j + 1) is B[j].
Return the minimum cost of repairing the roads such that all cities can be visited from city indexed (0, 0).
As the cost can be large, return the cost modulo 10^9+7.

Problem Constraints
1 <= N, M <= 10^5
1 <= A[i], B[i] <= 10^3

Example Input
Input 1:

 A = [1, 1, 1]
 B = [1, 1, 2]
Input 2:

 A = [1, 2, 3]
 B = [4, 5, 6]

Example Output
Output 1:
 16
Output 2:
 39
'''
# Add all the vertical (assign 1) and horizontal (assign 0) in an array
# Sort the array, v on the basis of the cost
# Run a loop and keep adding cost * m or n, whichever is smaller and reduce the m if we add row roads or reduce
# n if we add col roads.
class Solution:
    def solve(self, a, b):
        v = []
        for i in range(len(a)):
            v.append((a[i],1))
            
        for i in range(len(b)):
            v.append((b[i],0))
            
        v.sort()
        n = len(a)+1
        m = len(b)+1
        cost = 0
        for u in v:
            if u[1] == 0:
                cost += (u[0]*n)
                m -= 1
            else:
                cost += (u[0]*m)
                n -= 1
        return cost%(10**9 + 7)
# TC O(n*m)
# SC O(n*m)