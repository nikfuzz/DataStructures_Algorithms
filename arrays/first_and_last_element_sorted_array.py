''' 
Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
Follow up: Could you write an algorithm with O(log n) runtime complexity?

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]
'''

def searchRange(nums,target):
    # safety cases
    if nums == [] or len(nums) < 1:
        return [-1,-1]
    if len(nums) == 1 and target == nums[0]:
        return[0,0]
    
    # binary search to find the target
    l,r = 0, len(nums)-1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            # find left-most index
            l_i = mid
            while l_i>=0 and nums[l_i] == target:
                l_i -= 1
            # find right-most index
            r_i = mid
            while r_i<len(nums) and nums[r_i] == target:
                r_i += 1
            return [l_i+1, r_i-1]
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return[-1,-1]