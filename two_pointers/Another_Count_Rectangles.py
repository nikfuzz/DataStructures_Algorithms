'''
Another Count Rectangles

Given a sorted array of distinct integers A and an integer B, find and return how many rectangles with distinct configurations can be created using elements of this array as length and breadth whose area is lesser than B.
(Note that a rectangle of 2 x 3 is different from 3 x 2 if we take configuration into view)

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 109
1 <= B <= 109

Example Input
Input 1:
 A = [1, 2]
 B = 5

Input 2:
 A = [1, 2]
 B = 1


Example Output
Output 1:
 4

Output 2:
 0
'''

class Solution:
    def solve(self, a, b):
        m = 10**9 + 7
        i = 0
        j = len(a)-1
        count = 0
        while i <= j:
            # if the area is more than be then a[j] cannot be a part of the answer
            if (a[i]*a[j]) >= b:
                j -= 1
            else:
                # if the area is less for a[i] and a[j] then all the ans from j to i can be a part of the answer
                # we need to count the diff. and multiple by 2 for pairs like 3x2 and 2x3
                # -1 for pairs that have same index
                count += ((((j-i+1)*2)-1)%m)
                i+=1
        return count % m
# time complexity will be O(n)