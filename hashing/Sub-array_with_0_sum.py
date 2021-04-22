'''
Sub-array with 0 sum

Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
If the given array contains a sub-array with sum zero return 1 else return 0.

Problem Constraints
1 <= |A| <= 100000
-10^9 <= A[i] <= 10^9

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
Input 2:
 A = [-1, 1]


Example Output
Output 1:
 0
Output 2:
 1
'''

class Solution:
    # store the prefix sum in set
    # if any element reccurs in that set then the index of prev occ + 1 and curr occ
    # will give our subarray 
    def solve(self, a):
        sett = set()
        sett.add(0)
        s = 0
        for i in range(len(a)):
            s += a[i]
            if s not in sett:
                sett.add(s)
            else:
                return 1
        return 0
# TC O(n)
# SC O(n)
                
