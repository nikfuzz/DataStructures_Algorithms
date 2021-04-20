'''
Pairs with Given Difference

Given an one-dimensional integer array A of size N and an integer B.
Count all distinct pairs with difference equal to B.
Here a pair is defined as an integer pair (x, y), where x and y are both numbers in the array and their absolute difference is B.

Problem Constraints
1 <= N <= 104
0 <= A[i], B <= 105

Example Input
Input 1:
 A = [1, 5, 3, 4, 2]
 B = 3

Input 2:
 A = [8, 12, 16, 4, 0, 20]
 B = 4

Input 3:
 A = [1, 1, 1, 2, 2]
 B = 0


Example Output
Output 1:
 2

Output 2:
 5

Output 3:
 2
'''
class Solution:
    def solve(self, a, b):
        map = {}
        
        for i in range(len(a)):
            if a[i] in map:
                map[a[i]] += 1
            else:
                map[a[i]] = 1
        
        count  = 0
        a = set(a)
        a = list(a)
        for i in range(len(a)):
            # if b == 0 then we need to count all the elements which have a frequency more than 
            # count it just once because we need distinct pairs
            if b ==0 and map[a[i]]>1:
                count += 1

            # else just look for a[i] + b as (a[i] + some no == b)
            elif a[i]+b in map and map[a[i]+b] >= 1 and b>0:
                count += 1
        return count