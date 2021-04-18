'''
Pairs with given sum II

Given a sorted array of integers (not necessarily distinct) A and an integer B, find and return how many pair of integers ( A[i], A[j] ) such that i != j have sum equal to B.
Since the number of such pairs can be very large, return number of such pairs modulo (109 + 7).

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9
1 <= B <= 10^9

Example Input
Input 1:
A = [1, 1, 1]
B = 2

Input 2:
A = [1, 1]
B = 2


Example Output
Output 1:
 3

Output 2:
 1
'''

class Solution:
    # we will create a frequency arr or dictionary
    def solve(self, a, b):
        map = {}
        for i in range(len(a)):
            if a[i] not in map:
                map[a[i]] = 1
            else:
                map[a[i]] += 1
        count = 0
        # count all the occ of the num required for the pair and add it
        for i in range(len(a)):
            if b-a[i] in map:
                count += map[b-a[i]]
            # remove one if both the numbers are same
            if b-a[i] == a[i]:
                count -= 1
        return (count//2) % (10**9 + 7)
# time complexity O(n)
# space complexity O(n)