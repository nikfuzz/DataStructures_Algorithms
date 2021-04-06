'''
Special Integer

Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with sum of elements greater than B.

Problem Constraints
1 <= |A| <= 100000
1 <= A[i] <= 10^9
1 <= B <= 10^9

Input 1:
A = [1, 2, 3, 4, 5]
B = 10

Input 2:
A = [5, 17, 100, 11]
B = 130


Example Output
Output 1:
 2
Output 2:
 3
'''

class Solution:
    # two pointer approach
    # keep adding a[j] to sum
    # if sum exceeds b then keep subracting a[i] and i+= 1 until sum <= b
    # this will give us a window of the subarray that sol requires
    def solve(self, a, b):
        sum = 0
        i = 0
        n = len(a)
        ans = n
        
        for j in range(n):
            sum += a[j]
            while sum>b:
                sum -= a[i]
                i += 1
                
                ans = min(ans,(j-i)+1)
                if sum == 0:
                    break
                
            if sum == 0:
                return 0
        
                
        return ans