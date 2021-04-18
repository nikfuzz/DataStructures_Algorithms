'''
Subarray with given sum

Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
If the answer does not exist return an array with a single element "-1".
First sub-array means the sub-array for which starting index in minimum.

Problem Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 109


Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
 B = 5

Input 2:
 A = [5, 10, 20, 100, 105]
 B = 110


Example Output
Output 1:
 [2, 3]

Output 2:
 -1
'''

class Solution:
    def solve(self, a, b):
        i = 0
        j = 0

        sum = a[0]
        while i <= j and j<len(a):
            # if curr sum is greater than b then we know we cant another element to it
            # we need to remove ith element
            if sum>b:
                sum -= a[i]
                i += 1
            # if sum is less then we need to add jth element.
            # we dont dec i as those elements have been traversed
            elif sum < b:
                if j+1 >= len(a):
                    break
                j += 1
                sum += a[j]
            else:
                return a[i:j+1]
        return [-1]
# time complexity will be O(n)