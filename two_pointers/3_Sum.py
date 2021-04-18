'''
3 Sum

Given an array A of N integers, find three integers in A such that the sum is closest to a given number B. Return the sum of those three integers.
Assume that there will only be one solution.

Problem Constraints
-108 <= B <= 108
1 <= N <= 104
-108 <= A[i] <= 108

Example Input
Input 1:
A = [-1, 2, 1, -4]
B = 1

Input 2:
A = [1, 2, 3]
B = 6


Example Output
Output 1:
2

Output 2:
6
'''

class Solution:
# set one pointer, i which will iterate through the list
# we will set a start and end pointer between i and len(a)
# s and e will give us the second and third number
    def threeSumClosest(self, a, b):
        a.sort()
        curr = float('inf')
        for i in range(len(a)):
            s = i+1
            e = len(a)-1
            while s < e:
                sum = a[i] + a[s] + a[e]
                if sum == b:
                    return sum

                elif sum > b:
                    e -= 1

                else:
                    s += 1

                if abs(sum-b) < abs(curr-b):
                    curr = sum

        return curr
# O(n^2) time complexity
