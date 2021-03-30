'''
Pubg

There are N players each with strength A[i]. when player i attack player j, player j strength reduces to max(0, A[j]-A[i]). 
When a player's strength reaches zero, it loses the game and the game continues in the same manner among other players until only 1 survivor remains.
Can you tell the minimum health last surviving person can have?

constraints:
1 <= N <= 100000
1 <= A[i] <= 1000000

input: [6, 4]
output: 2

input: [2, 3, 4]
output: 1
'''

class Solution:
    def gcd(self,x,y):
        if x == 0:
            return y
        else:
            return self.gcd(y%x, x)
    
    # the lowest health would be the gcd of the arr
    def solve(self, a):
        if len(a) == 1:
            return a[0]
        
        gc = 0
        for i in range(len(a)):
            gc = self.gcd(gc,a[i])
            if gc == 1:
                return gc
        
        return gc


