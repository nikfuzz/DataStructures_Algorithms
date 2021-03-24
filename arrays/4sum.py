'''
4Sum
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.
Notice that the solution set must not contain duplicate quadruplets.

contraints:
0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

examples:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Input: nums = [], target = 0
Output: []

'''


def fourSum(a,k):
    # safety case
    if a == [] or len(a) < 4:
        return []
    res = []
    n = len(a)
    a.sort()
    for i in range(n-3):
        # to make sure elements are unique
        if i>0 and a[i] == a[i-1]:
            continue
        # we will mark i and j at the beginning and move two pointers from j+1 and from n-1 in opp directions
        # we will check for i+j+l+r
        for j in range(i+1,n-2):
            # to make sure elements are unique
            if j > i+1 and a[j] == a[j-1]:
                continue
            sum = a[i] + a[j]
            l = j+1
            r = n-1
            while l<r:
                if sum + a[l] + a[r] == k:
                    res.append([a[i], a[j], a[l], a[r]])
                    l += 1
                    r -= 1
                    # to make sure elements are unique
                    while l < r and a[l] == a[l-1]:
                        l += 1
                    while l < r and a[r] == a[r+1]:
                        r -= 1
                # if sum is less then inc l
                elif sum + a[l] + a[r] < k:
                    l += 1
                else:
                    r -= 1
    return res