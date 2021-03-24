''' 
Max Sum Contiguous Subarray

Find the contiguous subarray within an array, A of length N which has the largest sum.

Constraints:
1 <= N <= 1e6
-1000 <= A[i] <= 1000

input: [1, 2, 3, 4, -10] 
output: 10

input: [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
output: 6
'''

def maxSubArray(a):
    max_sum = curr_sum = a[0]
    # safety case
    if len(a) < 2:
        return max_sum
    # curr sum marks the beginning of our subarray
    # max sum marks the sum from the beginning to end of the sub array
    for i in range(1,len(a)):
        curr_sum = max(a[i], curr_sum + a[i])
        max_sum = max(curr_sum, max_sum)
    return max_sum