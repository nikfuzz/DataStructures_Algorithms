'''
Points on same line

Given two array of integers A and B describing a pair of (A[i], B[i]) coordinates in 2D plane. 
A[i] describe x coordinates of the ith point in 2D plane whereas B[i] describes the y-coordinate of the ith point in 2D plane.
Find and return the maximum number of points which lie on the same line.

Problem Constraints
1 <= (length of the array A = length of array B) <= 1000
-105 <= A[i], B[i] <= 105

Example Input
Input 1:
 A = [-1, 0, 1, 2, 3, 3]
 B = [1, 0, 1, 2, 3, 4]

Input 2:
 A = [3, 1, 4, 5, 7, -9, -8, 6]
 B = [4, -8, -3, -2, -1, 5, 7, -4]


Example Output
Output 1:
 4

Output 2:
 2
'''

# use slope to check for all the points
# store reduced form of numerator and denominator in a map
# the points which have same numerator/denominator will give us points on the same line
# also check for overlapping points and points which lie parallel to axis
class Solution:
    # gcd function
    def gcdCalculator(self,a,b):
        if a == 0:
            return b
        else:
            return self.gcdCalculator(b%a,a)
    
    
    def solve(self, a, b):
        n = len(a)
        ans = 0
        for i in range(n):
            overlaps = vertical = currmax = 0
            map = {}
            for j in range(i+1,n):
                if a[i] == a[j]:
                    if b[i] == b[j]:
                        overlaps += 1
                    else:
                        vertical += 1
                else:
                    numerator = b[j] - b[i]
                    denominator = a[j] - a[i]
                    # to convert in reduced form divide the numerator and denominator by their gcd
                    gcd = self.gcdCalculator(numerator, denominator)
                    numerator = numerator // gcd
                    denominator = denominator // gcd
                    
                    pair = tuple([numerator,denominator])
                    if pair not in map:
                        map[pair] = 1
                    else:
                        map[pair] += 1
                    currmax = max(currmax,map[pair])
                currmax = max(currmax,vertical)
            ans = max(currmax+overlaps+1,ans)
        return ans
# TC O(n^2) to compare all points with each other
# SC O(n^2) to store numerator and denominator for all points
