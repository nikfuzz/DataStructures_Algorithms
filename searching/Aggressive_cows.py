'''
Aggressive cows

Farmer John has built a new long barn, with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall, and an integer B which represent the number of cows.
His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

Problem Constraints
2 <= N <= 100000
0 <= A[i] <= 109
2 <= B <= N

Input 1:
A = [1, 2, 3, 4, 5]
B = 3

Input 2:
A = [1, 2]
B = 2

Output 1:
 2
Output 2:
 1
'''


class Solution:
    # we need to use binary search on the min distance between cows
    def check(self,a,b,m):
        # last position of the cow
        lp = a[0]
        # number of cows
        moo = 1
        for i in range(1,len(a)):
            if (a[i] - lp) >=m:
                moo += 1
                if moo == b:
                    return True
                lp = a[i]
        return False
        
    
    def solve(self, a, b):
        l = 0
        r = max(a)
        a.sort()
        ans = 0
        while l<=r:
            m = (l+r)//2
            
            if self.check(a,b,m):
                l = m+1
                ans = m
            else:
                r = m-1
        return ans
                    