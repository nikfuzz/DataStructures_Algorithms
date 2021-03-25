'''
Make Sum Divisible by P

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.
Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.
A subarray is defined as a contiguous block of elements in the array.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= p <= 109

Input: nums = [6,3,5,2], p = 9
Output: 2

Input: nums = [1,2,3], p = 3
Output: 0

Input: nums = [1,2,3], p = 7
Output: -1

Input: nums = [1000000000,1000000000,1000000000], p = 3
Output: 0
'''

def minSubarray(nums, p):
    r = sum(nums)%p
    # safety cases
    if r == 0:
        return 0
    if sum(nums) < p:
        return -1
    map = {}
    map[0] = -1
    mi = float('inf')
    s = 0
    # we will create a prefix sum and get key for each element 
    for i in range(len(nums)):
        s += nums[i]
        # need to check which subarray contributes to the sum(nums)%p, that way we can remove it and make sum(nums)%p == 0
        key = (s%p) - r
        # to convert keys that are neg to pos, k%=p == k += p
        key %= p
        if key in map:
            mi = min(mi, i-map[key])
        map[s%p] = i
    if mi != float('inf') and mi != len(nums):
        return mi
    return -1